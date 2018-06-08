#!/usr/bin/env python3
#  coding=utf-8
import argparse
from mapping.utils import read_lines


parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
parser.add_argument("-s", "--set", dest="name", metavar="NAME", help="set the track name")
args = parser.parse_args()

for f in args.files:
    for line in read_lines(f):
        print(line)

# cnt = 1
# while line:
#     print("Line {}: {}".format(cnt, line.strip()))
#     line = fp.readline()
#     cnt += 1
#         while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data

# def read_remap_file(file):
