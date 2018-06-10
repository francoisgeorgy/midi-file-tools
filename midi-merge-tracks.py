#!/usr/bin/env python3
# coding=utf-8

import argparse
import mido
from utils.misc import suffixFilename


parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
# parser.add_argument("-s", "--set", dest="name", metavar="NAME", help="set the track name")
args = parser.parse_args()

multiple_files = len(args.files) > 1

for f in args.files:

    mid = mido.MidiFile(f)

    if multiple_files:
        print('::::::::::::::')
        print(f)
        print('::::::::::::::')

    merged_track = mido.merge_tracks(mid.tracks)

    merged_mid = mido.MidiFile(type=0)

    merged_mid.tracks.append(merged_track)

    nf = suffixFilename(f, '_merged')
    print(f, '-->', nf)

    merged_mid.save(nf)
