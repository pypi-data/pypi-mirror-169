import inspect
import logging
import os
from argparse import Namespace
from logging import handlers
from pathlib import Path
import argparse
import sys
from enum import Enum
import configparser
from builtins import property

import paramiko
import paramiko.client
from paramiko import Transport, sftp_client
from log_ocr.GbOcrTrack import GbOcrTracker

# For logging activity
GB_LOG_HOME_ENV_KEY = "RUN_ACTIVITY_LOG_HOME"
# Config file environment variable
GB_CONFIG_PATH_ENV_KEY: str = "GB_CONFIG"


class GbArgs:
    """
    @DynamicAttrs
    """
    # Thanks to https://stackoverflow.com/questions/30334160/
    # disabling-pycharm-unresolved-references-inspection-for-attribute-names-but-not


class GbSftpConfig:
    """
    Created on 15 Jun 2022

    Wrapper for a dbConfig file whose format is:
    [default]
    port = "value"
    user = "value"
    host = "value"
    key_path = "value"

    [section]
    port = "value"
    user = "value"
    host = "value"
    key_path = "value"
    ...
    Any key not in 'section' can be fetched from the default

    @author: jsk

    """

    # private variables
    _default_section_name = "default"
    _port_key = "port"  # Tip of the hat to Harry Potter
    _user_key = "user"
    _host_key = "host"
    _key_file_key = "keyFile"
    _gpg_passphrase_key = "gpgPass"
    _configFQPath = None
    _configParser = None
    _operationSection = None

    def __init__(self, type_section: str = "default", config_file_name: str = None):
        """
        Google Books SFTP description
        :param type_section: Optional, can set with section property
        :param config_file_name: initial file - Optional: can set with config_file_name property
        """
        self.op_section = type_section

        global GB_CONFIG_PATH_ENV_KEY
        import os
        if config_file_name is None:
            config_file_name: str = os.getenv(GB_CONFIG_PATH_ENV_KEY)
            if config_file_name is None:
                raise ValueError(f" environment variable {GB_CONFIG_PATH_ENV_KEY} expected, but not set")
        self.config_file_name = config_file_name

    # --------------------------------------------------------------------------

    @property
    def config_file_name(self):
        """Config file we are parsing"""
        return self._configFQPath

    @config_file_name.setter
    def config_file_name(self, value):
        """Set the name of the gb_Config file"""

        # unset the current
        if value is None:
            self._configFQPath = None
            self._configParser = None
            return

        cfgPath = Path(value)
        if cfgPath.is_file():
            self._configFQPath = str(cfgPath)
            # Rebuild the _parser
            self._parser(self._configFQPath)
        else:
            # On error, keep existing value
            raise FileNotFoundError(str(cfgPath))

    # --------------------------------------------------------------------------

    @property
    def op_section(self):
        """A section in the config file"""
        return self._operationSection

    @op_section.setter
    def op_section(self, value):
        self._operationSection = value

    # --------------------------------------------------------------------------

    @property
    def port(self) -> int:
        """
        host port
        :return: configured port
        """
        _ = self.get_value(self._port_key)
        return -1 if _ == '' else int(_)

    # --------------------------------------------------------------------------

    @property
    def host(self) -> str:
        """
        host name or IP
        :return: name or IP
        """
        return self.get_value(self._host_key)

    # --------------------------------------------------------------------------

    @property
    def user(self) -> str:
        """
        host name or IP
        :return: name or IP
        """
        return self.get_value(self._user_key)

    # --------------------------------------------------------------------------

    @property
    def key_path(self) -> str:
        """
        host name or IP
        :return: name or IP
        """
        return self.get_value(self._key_file_key)

    # --------------------------------------------------------------------------
    @property
    def gpg_passphrase(self) -> str:
        """
        Return a gpg passphrase
        :return:
        """
        return self.get_value(self._gpg_passphrase_key)

    # --------------------------------------------------------------------------

    def _parser(self, file_name):
        """
        Creates a dbConfig _parser from file_name
        """
        self._configParser = configparser.ConfigParser()
        self._configParser.read(file_name)

    # --------------------------------------------------------------------------

    def test_init(self):
        """Tests for variable setup before action"""
        if not self.op_section \
                or not self._configParser:
            raise ValueError

            #

    # --------------------------------------------------------------------------
    def get_value(self, key: str) -> str:
        """
        :param key:
        :return:  either the current section's entry for the key, or the default
        section, if there is none
        """
        self.test_init()
        rs: str = ""
        try:
            rs = self._configParser[self.op_section][key]
        except KeyError:
            try:
                rs = self._configParser[self._default_section_name][key]
            except KeyError:
                pass
        return rs

    # Override
    def __str__(self):
        return f"config_file_name: {self.config_file_name} section:{self.op_section} port:{self.port} " \
               f"host:{self.host} user:{self.user} key:{self.key_path} "


class GbParserBase(argparse.ArgumentParser):
    """
    Required functionality for all google books command line parsers
    """

    def __init__(self, *args, **kwargs):
        super(GbParserBase, self).__init__(*args, **kwargs)

        # Everyone gets these
        self.add_argument("-l", "--log_home", help="Where logs are stored - see manual",
                          default=os.getenv(GB_LOG_HOME_ENV_KEY))
        self.add_argument("-n", "--dry_run", help="Connect only. Do not upload", action="store_true", default=False)

        self.add_argument("-d",
                          "--debug_level",
                          dest='debug_level',
                          action='store',
                          choices=self._debug_choices.keys(),
                          default='info',
                          help="choice values are from python logging module")
        self.add_argument("-x",
                          "--log_level",
                          action="store",
                          nargs='?',
                          help=argparse.SUPPRESS,
                          default=logging.INFO)
        self.add_argument("-z",
                          "--log_after_fact",
                          action="store_true",
                          help="(ex post facto) log a successful activity after it was performed out of band ",
                          default=False)

        # Tip o the hat to https://gist.github.com/martinth/ed991fb8cdcac3dfadf7
        # for showing how to read from a list of files, or stdin, using fileinput module
        self.add_argument("-i", "--input_file", metavar='FILE', nargs='?', help='files to read. use -  for stdin ')

    _debug_choices = {'info': logging.INFO,
                      'warning': logging.WARN,
                      'error': logging.ERROR,
                      'debug': logging.DEBUG,
                      'critical': logging.CRITICAL}

    def init(self) -> Namespace:
        """
        Parses and handles downstream actions - logging
        :return: parsed_args object
        """
        args = self.parse_args()
        args.log_level = self._debug_choices[args.debug_level]
        return args


class GbFtpOps(str, Enum):
    """
    Universe of supported FTP operations
    """
    GET_OP = "get"
    PUT_OP = "put"


class GbSftp:
    """
    Handles Google Books SFTP operations.
    """

    def __init__(self, content_type: str, dry_run: bool = False):
        """
        Set up the config
        :param content_type: destination content_type (for config)
        :param dry_run: True if diagnostic connection only
        """
        self._content_type = content_type
        self._dry_run = dry_run

        self._config = GbSftpConfig(type_section=self._content_type)

        self._log = logging.getLogger('ftp_op')
        # ftp_log = logging.getLogger(run_logger_name)
        self._log.debug("%s", self._config)
        self.open()

    _content_type: str = ""
    _dry_run: bool = False
    _config: GbSftpConfig = None
    _log: logging = None
    _sftp_client: sftp_client.SFTPClient = None

    @property
    def dest(self):
        return self._content_type

    def op(self, op_call, op_name: str, local_file: str, remote_file: str):
        """
        Perform a put or a get
        :param op_call: routine to execute
        :param op_name: descriptive
        :param local_file:
        :param remote_file:
        :return:
        """
        isSuccess: bool = True
        log = self._log

        try:
            if not self._dry_run:
                if callable(op_call):
                    attrs = op_call(localpath=local_file, remotepath=remote_file)
                    log.debug(f"{attrs}")
                log.info(f"{op_name}:{local_file} to {remote_file}")
            else:
                log.info(f"(dry-run){op_name}:{local_file} to {remote_file}")

        except paramiko.SSHException:
            esi = sys.exc_info()
            log.error(f"{op_name}:Failed {local_file} to {remote_file}, {str(esi[1])}")
            isSuccess = False
        except IOError:
            ei = sys.exc_info()
            self._log.error(f"{ei[1]}")
            isSuccess = False

        return isSuccess

    def put(self, local_file: str, remote_file: str) -> bool:
        """
        returns success of sftp put call
        :param local_file: object to put
        :param remote_file: destination path (relative to remote site logon dir)
        :return:
        """
        return self.op(self._sftp_client.put, str(GbFtpOps.PUT_OP), local_file, remote_file)

    def get(self, local_file: str, remote_file: str) -> bool:
        """
        returns success of sftp get call
        :param local_file: object to put
        :param remote_file: destination path (relative to remote site logon dir)
        :return:
        """
        return self.op(self._sftp_client.get, str(GbFtpOps.GET_OP), local_file, remote_file)

    def open(self):
        """
        Create the connection
        :return:
        """

        r"""
           Take 1 log:
               Attempting public-key auth...
               DEB [20220601-15:06:58.802] thr=1   paramiko.transport: u
               DEB [20220601-15:06:58.714] thr=1   paramiko.transport: Switch to new keys ...
           DEB [20220601-15:06:58.715] thr=2   paramiko.transport: Attempting public-key auth...
           DEB [20220601-15:06:58.802] thr=1   paramiko.transport: userauth is OK
           DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Finalizing pubkey algorithm for key of content_type 
                       'ssh-rsa'
           DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Our pubkey algorithm list: 
                       ['rsa-sha2-512', 'rsa-sha2-256', 'ssh-rsa']
           DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Server did not send a server-sig-algs list; 
                       defaulting to our first preferred algo ('rsa-sha2-512')
           DEB [20220601-15:06:58.802] thr=1   paramiko.transport: NOTE: you may use the 'disabled_algorithms' 
                       SSHClient/Transport init kwarg to disable that or other algorithms if your server does not 
                       support them!
           INF [20220601-15:06:58.896] thr=1   paramiko.transport: Authentication (publickey) failed.

            --jimk-- and use the disabled_algorithms in this argument. I believe that the arguments
            we pass (see "ourpubkey list = ['rsa-sha2-512', 'rsa-sha2-256', 'ssh-rsa'] is what's breaking.
            Using the advice to put the first two on the 'disabled_algorithms' list should send only 'ssh-rsa'
            which ought to work.

            It did  
           """
        #
        # SFTP
        # 1. Transport
        # 2. Channel - opened using transport
        # ftp = paramiko.client.SSHClient()
        # ftp.set_missing_host_key
        # Take 2 https://www.reddit.com/r/learnpython/comments/sixjay/how_to_use_disabled_algorithms_in_paramiko/

        log = self._log
        sock: () = (self._config.host, self._config.port,)

        # Specific to GB hosts
        disabled_algorithms: {} = {'pubkeys': ['rsa-sha2-512', 'rsa-sha2-256']}

        sftp_transport: Transport = Transport(sock=sock, disabled_algorithms=disabled_algorithms)
        _pkey = paramiko.RSAKey.from_private_key_file(self._config.key_path)

        try:
            sftp_transport.connect(pkey=_pkey, username=self._config.user)
            log.debug(f"Connected to {self._config.host} ")
            self._sftp_client = sftp_client.SFTPClient.from_transport(sftp_transport)
            log.debug(f"created client")
        except paramiko.SSHException:
            ei = sys.exc_info()
            log.error(f":open:Could not connect to host. Internal exception: {str(ei[1])}")


def print_args(args: argparse.Namespace) -> str:
    return str([(i[0], i[1],) for i in inspect.getmembers(args) if not i[0].startswith('_')])
