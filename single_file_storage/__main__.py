#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import argparse
import os
import sys

from single_file_storage import help
from single_file_storage import storage

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


def main():
    parser = argparse.ArgumentParser(f"{help.get_name()} {help.get_version()} ({help.get_source_url()})")
    parser.add_argument('-data', '--data', default='./dataa', type=str, help='data storage path', required=False)
    parser.add_argument('-port', '--port', default=8082, type=int, help='http proxy port', required=False)
    parser.add_argument('-users', '--users', type=lambda s: dict(item.split('=') for item in s.split(',')),
                        help='user & passwd')
    args = parser.parse_args()
    storage.users = args.users if args.users is not None else storage.users
    storage.DATA_PATH = args.data if args.data is not None else storage.DATA_PATH
    storage.start(port=args.port)


if __name__ == "__main__":
    main()
