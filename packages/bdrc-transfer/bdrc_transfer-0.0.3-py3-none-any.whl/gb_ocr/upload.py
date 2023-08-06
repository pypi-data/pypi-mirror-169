#!/usr/bin/env python3

"""
SFTP upload specific to Google Books
"""
import argparse
import os
import pathlib
from logging import handlers
from pathlib import Path

import paramiko
import paramiko.client
from paramiko import Transport, sftp_client

import sys
from googleBooksUpload.gb_config.GBSFTPconfig import GBSFTPConfig

import logging

GB_CONFIG_PATH_ENV_KEY: str = "GB_CONFIG"
run_logger_name = 'upload_logger'


def upload(dest: str, local_file: str, dry_run: bool) -> bool:
    """
    :rtype: bool
    :type dest: string
    :param: dest  -- proxy for location. Name of a section in the config file
    Uploads a metadata file to one of the  GB Partner sites
    :param local_file: path to file to upload
    :param dry_run: true if connect only
    :return:
    """

    # only log errors to the runtime logger
    global run_logger_name

    ftp_load_log = logging.getLogger()
    # ftp_load_log = logging.getLogger(run_logger_name)

    global GB_CONFIG_PATH_ENV_KEY
    config_file_path: str = os.getenv(GB_CONFIG_PATH_ENV_KEY)
    gb_config = GBSFTPConfig(config_file_name=config_file_path, op_section=dest)

    ftp_load_log.debug("%s", gb_config)

    r"""
    Take 1 log:
        Attempting public-key auth...
        DEB [20220601-15:06:58.802] thr=1   paramiko.transport: u
        DEB [20220601-15:06:58.714] thr=1   paramiko.transport: Switch to new keys ...
    DEB [20220601-15:06:58.715] thr=2   paramiko.transport: Attempting public-key auth...
    DEB [20220601-15:06:58.802] thr=1   paramiko.transport: userauth is OK
    DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Finalizing pubkey algorithm for key of type 'ssh-rsa'
    DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Our pubkey algorithm list: ['rsa-sha2-512', 'rsa-sha2-256', 'ssh-rsa']
    DEB [20220601-15:06:58.802] thr=1   paramiko.transport: Server did not send a server-sig-algs list; defaulting to our first preferred algo ('rsa-sha2-512')
    DEB [20220601-15:06:58.802] thr=1   paramiko.transport: NOTE: you may use the 'disabled_algorithms' SSHClient/Transport init kwarg to disable that or other algorithms if your server does not support them!
    INF [20220601-15:06:58.896] thr=1   paramiko.transport: Authentication (publickey) failed.
    
        
     --jimk-- and use the disabled_algorithms in this argument. I believe that the arguments
     we pass (see "ourpubkey list = ['rsa-sha2-512', 'rsa-sha2-256', 'ssh-rsa'] is what's hoerking.
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

    isSuccess = True
    remote_file: str = Path(local_file).name

    sock: () = (gb_config.host, gb_config.port,)

    # Specific to GB hosts
    disabled_algorithms: {} = {'pubkeys': ['rsa-sha2-512', 'rsa-sha2-256']}

    gb_sftp_client: sftp_client.SFTPClient

    sftp_transport: Transport = Transport(sock=sock, disabled_algorithms=disabled_algorithms)
    _pkey = paramiko.RSAKey.from_private_key_file(gb_config.key_path)

    try:
        sftp_transport.connect(pkey=_pkey, username=gb_config.user)
        gb_sftp_client = sftp_client.SFTPClient.from_transport(sftp_transport)
        try:

            if not dry_run:
                attrs = gb_sftp_client.put(localpath=local_file, remotepath=remote_file)
                ftp_load_log.info(f"Put {local_file} to {remote_file}")
                ftp_load_log.debug(f"{attrs}")
            else:
                ftp_load_log.info(f"(dry-run) put {local_file} to {remote_file}")

            ftp_load_log.debug(f'{gb_sftp_client.listdir(".")}')
        except paramiko.SSHException:
            esi = sys.exc_info()
            ftp_load_log.error(f"Failed put {local_file} to {remote_file}, {str(esi[1])}")
            isSuccess = False
        finally:
            gb_sftp_client.close()
    except paramiko.SSHException:
        ei = sys.exc_info()
        ftp_load_log.error(f"Could not connect to host. Internal exception: {str(ei[1])}")
        isSuccess = False

    return isSuccess


def setup_log(log_root: str) -> ():
    """
    Set up two loggings: progress/diagnostic logging to the console and a file,
    and tracking logging, which logs the individual activity
    :return:
    """

    # root  logger
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("paramiko").setLevel(logging.ERROR)

    # Each individual run is not important, so accumulate them in a log
    instance_id_log_path = f"SFTPUpload-runtime.log"

    basic_formatter = logging.Formatter(fmt='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m-%d %H:%M')
    # More time, fewer other details in activity
    activity_formatter = logging.Formatter(fmt='%(asctime)s:%(message)s', datefmt='%m-%d-%Y %H-%M-%S')

    # Get the logger
    global run_logger_name
    # will this just get the root logger?
    runtime_logger = logging.getLogger()
    # runtime_logger = logging.getLogger(run_logger_name)
    # add a console handler to the runtime logger
    # Not needed - the console is where the root logger goes.
    console = logging.StreamHandler()
    console.setFormatter(basic_formatter)
    #    runtime_logger.addHandler(console)

    file_handler = handlers.RotatingFileHandler(Path(log_root, instance_id_log_path), maxBytes=4096000, backupCount=100)

    # file_handler = logging.FileHandler(Path(log_root, f"{instance_id_log_path}"))
    file_handler.setFormatter(basic_formatter)
    runtime_logger.addHandler(file_handler)

    activity_logger = logging.getLogger('activity')
    # Dont rotate file
    activity_file_handler = logging.FileHandler(Path(log_root, 'SFTPUpload-activity.log'))
    activity_file_handler.setLevel(logging.INFO)
    activity_file_handler.setFormatter(activity_formatter)
    activity_logger.addHandler(activity_file_handler)

    return (runtime_logger, activity_logger,)


if __name__ == "__main__":

    ap = argparse.ArgumentParser(
        description="Uploads a file to a specific partner server, defined by a section in the config file")
    destinations = ap.add_mutually_exclusive_group()
    destinations.add_argument("-m", "--metadata", help="Send to the metadata target", action="store_true")
    destinations.add_argument("-c", "--content", help="Send to the content target", action="store_true")
    ap.add_argument_group(destinations)
    ap.add_argument("-l", "--log_home", help="Where logs are stored - default: working dir",
                    default=os.getcwd())
    ap.add_argument("-n", "--dry_run", help="Connect only. Do not upload", action="store_true", default=False)
    ap.add_argument("src", help="source file to upload")

    parse_args = ap.parse_args()
    dest_token = "metadata" if parse_args.metadata else "content"
    paths: str = f"{parse_args.src}:{dest_token}"

    run_log, activity_log = setup_log(parse_args.log_home)

    if not os.access(str(parse_args.log_home), os.W_OK):
        error_string: str = f"logging directory {parse_args.log_home} is not  writable or does not exist"
        run_log.error(error_string)
        activity_log.error("%s:log home %s not found or writable:%s", "error", parse_args.src, dest_token)
        raise NotADirectoryError(parse_args.log_home)

    if not pathlib.Path.exists(Path(parse_args.src)) or not os.access(parse_args.src, os.R_OK):
        run_log.error(f"Errno 2: source {parse_args.src} not found or not readable")
        activity_log.error("error:source %s not found or readable:%s", parse_args.src, dest_token)
        raise FileNotFoundError(parse_args.src)

    upload_args = {
        'dest': dest_token,
        'local_file': parse_args.src,
        'dry_run': parse_args.dry_run
    }
    allOk: bool = upload(**upload_args)

    if allOk:
        run_log.info("upload success %s:s", parse_args.src, dest_token)
        activity_log.info("success:%s:%s", parse_args.src, dest_token)
    else:
        run_log.error("upload failed %s:%s", parse_args.src, dest_token)
        activity_log.error("error:%s:%s:", parse_args.src, dest_token)
