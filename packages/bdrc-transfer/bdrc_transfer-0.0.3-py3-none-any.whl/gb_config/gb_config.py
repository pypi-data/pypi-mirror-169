#!/usr/bin/env python3
"""
Google Books GRIN initial setup script
- Copy grin config from install directory to user's ~/.config/gb directory
"""
import shutil
from inspect import getsourcefile
import os
from pathlib import Path

cfg_file_name = 'grin.config'

def config_main():
    """
    Configure google books process. Mostly load the Google Books non-confidential config file
    variables
    :return:
    """
    where_am_i = getsourcefile(config_main)
    config_src: Path = Path(where_am_i).parent / cfg_file_name
    config_dest: Path =  Path(Path.home(), '.config', 'gb')
    os.makedirs(name = config_dest, exist_ok = True, mode = 0o700 )
    print(f'Copying config to user path {str(config_dest)}')
    shutil.copyfile(config_src, config_dest / cfg_file_name)

# Uncomment for testing
# config_main()