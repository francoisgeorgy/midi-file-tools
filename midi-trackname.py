#!/usr/bin/env python3
# coding=utf-8

import argparse
import mido

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
parser.add_argument("-s", "--set", dest="name", metavar="NAME", help="set the track name")
args = parser.parse_args()

multiple_files = len(args.files) > 1

for f in args.files:
    mid = mido.MidiFile(f)
    for i, track in enumerate(mid.tracks):

        if multiple_files:
            print("{}: {}".format(f, track.name), end='')
        else:
            print(track.name, end='')

        if args.name:
            track.name = args.name
            mid.save(f)
            print(" --> {}".format(args.name))
        else:
            print()
