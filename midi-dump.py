#!/usr/bin/env python3
# coding=utf-8

import argparse
import mido

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
parser.add_argument("-m", "--meta", action="store_true", help="dump only meta informations")
args = parser.parse_args()

multiple_files = len(args.files) > 1

for f in args.files:
    if multiple_files:
        print("::::::::::::::")
        print(f)
        print("::::::::::::::")
    mid = mido.MidiFile(f)
    for i, track in enumerate(mid.tracks):
        print("Track {}: {}".format(i, track.name))
        for msg in track:
            if args.meta:
                if msg.is_meta:
                    print(msg)
            else:
                print(msg)
