#!/usr/bin/env python3
"""
Requests download of an OCR'd image group
"""
import argparse
import fileinput
import logging
import sys

from gb_lib import GbLib as lib

activity: str = "download"
dest_token: str = "content"

run_log: logging
activity_log: logging


def download(image_group: str, args: argparse.Namespace):
    """
    Does real work
    :param image_group:
    :param args: options
    :return:
    """
    if args.log_after_fact:
        run_log.info(f"Simulating {activity} for {image_group}:{dest_token}")
        activity_log.info(f"success:{activity}:{image_group}:{dest_token}")
        return


def download_main():
    ap = lib.GbParserBase(
        description="Downloads an OCR'd content image group")
    ap.add_argument("image_group", help="workRid-ImageGroupRid - no file suffixes", nargs='?')

    parsed_args: argparse.Namespace = ap.init()
    _app_logger = lib.AORunActivityLog(prefix=activity, home=parsed_args.log_home, level=parsed_args.log_level)

    global run_log, activity_log
    run_log = _app_logger.runtime_logger
    activity_log = _app_logger.activity_logger

    run_log.debug(f"args: {lib.print_args(parsed_args)}")

    if parsed_args.input_file:
        for f in fileinput.input(files=parsed_args.input_file):
            download(f.strip(), parsed_args)
        return
    download(parsed_args.src, parsed_args)


if __name__ == "__main__":
    download_main()

