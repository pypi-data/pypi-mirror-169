#!/usr/bin/env python3
"""
Translate html to json
"""

import sys
from lxml import etree


def parse_gb(file_path: str) -> str:
    dom = etree.parse(file_path)

# https://stackoverflow.com/questions/40618625/using-xpath-in-python-with-lxml