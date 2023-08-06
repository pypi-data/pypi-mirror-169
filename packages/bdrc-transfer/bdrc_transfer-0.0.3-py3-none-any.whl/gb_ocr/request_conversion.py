#!/usr/bin/env python3
"""
Requests conversion of an image group. Will have to fill in with gb auth.
Note that a network trace of the POST data for selecting some barcodes and clicking submit
gives:
(target URL is /libraries/TBRC/_process
Document_process
1 / 7 requests
3.6 kB / 47.5 kB transferred
3.6 kB / 122 kB resources
Finish: 611 ms
DOMContentLoaded: 406 ms
Load: 501 ms
process_format=html
&barcodes=W1PD159424-I3PD77
&barcodes=W1PD159424-I3PD80
&barcodes=W1PD159424-I3PD87
&barcodes=W1PD159424-I3PD89
&barcodes=W1PD159424-I3PD90
&table_result_count=%2Flibraries%2FTBRC%2F_available%3Fresult_count%3D50
(decoded: /libraries/TBRC/_available?result_count=50)
"""
import argparse
import fileinput
from log_ocr.AORunLog import AORunActivityLog

from gb_lib import GbLib as lib

activity: str = "request_conversion"
dest_token: str = "content"

log: AORunActivityLog


def request_one(image_group: str, args: argparse.Namespace):
    """

    :param image_group: image group to request
    :param args:
    :return: system settings
    """

    # Seriously, hurl if this doesn't work
    work_name: str = image_group.split('-')[0]
    if args.log_after_fact:
        log.runtime_logger.info(f"Simulating {activity} for {image_group}:{dest_token}")
        log.activity_logger.info(f"success:{activity}:{image_group}:{dest_token}")
        log.activity_db_logger.add_content_activity(work_rid=work_name, activity=activity,
                                                    image_group_label=image_group, upload_rc=0)
        return


def request_conversion_main():
    global log

    ap = lib.GbParserBase(
        description="Requests conversion of an uploaded content image group")
    ap.add_argument("image_group", help="workRid-ImageGroupRid - no file suffixes", nargs='?')

    parsed_args: argparse.Namespace = ap.init()

    log = AORunActivityLog(prefix=activity, home=parsed_args.log_home, level=parsed_args.log_level)
    log.runtime_logger.debug(f"args: {lib.print_args(parsed_args)}")

    if parsed_args.input_file:
        for f in fileinput.input(files=parsed_args.input_file):
            request_one(f.strip(), parsed_args)
        return

    request_one(parsed_args.image_group, parsed_args)


if __name__ == "__main__":
    request_conversion_main()
