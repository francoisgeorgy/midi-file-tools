#!/usr/bin/env python3
# coding=utf-8

#TODO: allow the user to give his own map for the notes names
#TODO: choose map according to the note's channel

import argparse
import mido
from mapping.maps import midi_map

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
parser.add_argument("-m", "--map", dest="mapping", choices=["inst", "perc"], metavar="MAP", help="set the mapping to use for the notes names. Must be inst or perc.")
args = parser.parse_args()

if args.mapping is None:
    mapping = midi_map["GM_Level-1_Instruments"]
elif args.mapping == "inst":
    mapping = midi_map["GM_Level-1_Instruments"]
elif args.mapping == "perc":
    mapping = midi_map["GM_Level-1_Percussions"]
else:
    print("invalid mapping")
    exit()

multiple_files = len(args.files) > 1

notes = []

for f in args.files:
    if multiple_files:
        print("::::::::::::::")
        print(f)
        print("::::::::::::::")
    mid = mido.MidiFile(f)
    for track in mid.tracks:
        for msg in track:
            if msg.is_meta:
                continue
            if msg.type != "note_on":
                continue
            if msg.note not in notes:
                notes.append(msg.note)

notes.sort()

for note in notes:
    if note in mapping:
        print(note, mapping[note])
    else:
        print(note, "/!\\ UNKNOWN INSTRUMENT")
