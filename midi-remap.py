#!/usr/bin/env python3
# coding=utf-8

# remap file format: <FROM-NOTE-NUMBER> <TO-NOTE-NUMBER> <OPTIONAL-COMMENT>

import argparse
import mido
from mapping.utils import read_remap
from utils.misc import suffixFilename


parser = argparse.ArgumentParser()
parser.add_argument("map", help="file containing the mapping rules")
parser.add_argument("-c", "--channel", type=int, default=-1, dest="channel", metavar="CHANNEL", help="set the channel for the remapped notes")
parser.add_argument("-t", "--track", type=int, default=-1, dest="track", metavar="TRACK", help="only remap this track")
parser.add_argument("file", nargs="+")
args = parser.parse_args()

remap = read_remap(args.map)

multiple_files = len(args.file) > 1

for f in args.file:

    if multiple_files:
        print('::::::::::::::')
        print(f)
        print('::::::::::::::')

    mid = mido.MidiFile(f)

    for i, track in enumerate(mid.tracks):
        if 0 <= args.track != i:
            continue
        for msg in track:
            if msg.is_meta:
                continue
            if msg.type not in ('note_on', 'note_off'):
                continue

            if args.channel >= 0:
                msg.channel = args.channel

            for m in remap:
                if m['from'] == msg.note:
                    msg.note = m['to']

    nf = suffixFilename(f, '_remapped')
    print(f, '-->', nf)

    mid.save(nf)



