"""
Created on June 4, 2022

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
import configparser
from pathlib import Path
from builtins import property


class GBSFTPConfig:
    """
    :summary: Read GB Config file
    :param config_file_name: Fully qualified path to GoogleBooks SFTP file
    """

    # private variables
    _default_section_name = "default"
    _port_key = "port"  # Tip of the hat to Harry Potter
    _user_key = "user"
    _host_key = "host"
    _key_file_key = "keyFile"
    _configFQPath = None
    _configParser = None
    _operationSection = None

    def __init__(self, op_section: str = None, config_file_name: str = None):
        """
        Google Books SFTP description
        :param initial op section: Optional, can set with section property
        :param config_file_name: initial file - Optional: can set with config_file_name property
        """
        self.op_section = op_section
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
        return int(self.get_value(self._port_key))

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
        return f"config_file_name: {self.config_file_name} section:{self.op_section} port:{self.port} host:{self.host} user:{self.user} key:{self.key_path}"

