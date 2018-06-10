#!/usr/bin/env python3
# coding=utf-8

import argparse
import mido
# from mido import MetaMessage

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
args = parser.parse_args()

multiple_files = len(args.files) > 1

for f in args.files:

    mid = mido.MidiFile(f)

    if multiple_files:
        print('::::::::::::::')
        print(f)
        print('::::::::::::::')

    for i, track in enumerate(mid.tracks):

        print("track {}".format(i))

        print("   name: {}".format(track.name))

        notes = []
        channels = []

        for msg in track:

            if msg.is_meta and msg.type == 'instrument_name':
                print("   inst: {}".format(msg.name))

            if msg.is_meta:
                continue
            if msg.type != "note_on":
                continue
            if msg.note not in notes:
                notes.append(msg.note)
            if msg.channel not in channels:
                channels.append(msg.channel)

        notes.sort()
        channels.sort()

        print("   notes: {}".format(notes))
        print("   channels: {}".format(channels))

