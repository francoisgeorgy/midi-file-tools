#!/usr/bin/env python3
# coding=utf-8

import argparse
from pathlib import Path
import mido

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
parser.add_argument("-t", "--track", dest="tracknumber", metavar="TRACKNUMBER", type=int, help="the number (from 1) of the track to copy")
parser.add_argument("-tn", "--trackname", dest="trackname", metavar="TRACKNAME", help="set the track name")
parser.add_argument("-an", "--artistname", dest="artistname", metavar="ARTISTNAME", help="set the artist name")
args = parser.parse_args()

multiple_files = len(args.files) > 1

track_number = (args.tracknumber - 1) if args.tracknumber else 0
if track_number < 0: track_number = 0
#track_name = args.trackname if args.trackname else None
artist_name = args.artistname if args.artistname else ''

for f in args.files:

    mid = mido.MidiFile(f)

    if track_number > len(mid.tracks):
        print("Invalid track number: file %s has only %d track(s)" % (f, len(mid.tracks)))
        continue

    # tries to find time signature and tempo:

    time_signature = None
    set_tempo = None
    for m in mid.tracks[0]:
        if m.is_meta:
            if m.type == 'time_signature':
                time_signature = m
                break
    for m in mid.tracks[0]:
        if m.is_meta:
            if m.type == 'set_tempo':
                set_tempo = m
                break

    if args.trackname:
        track_name = args.trackname
    else:
        for m in mid.tracks[0]:
            if m.is_meta:
                if m.type == 'track_name':
                    track_name = m.name
                    break
    if not track_name:
        track_name = 'no name'

    new_track = mid.tracks[track_number]

    if time_signature:
        new_track.insert(0, time_signature)
    if set_tempo:
        new_track.insert(0, set_tempo)

    new_track.name = track_name

    # XF track name and artist name
    new_track.insert(0, mido.MetaMessage('text', text='XFln:L1:' + track_name + ':Composer:::' + artist_name + ':'))

    # XF Version ID
    new_track.insert(0, mido.MetaMessage('sequencer_specific', data=[0x43, 0x7B, 0, 0x58, 70, 48, 50, 0, 1]))

    new_mid = mido.MidiFile(type=0)

    new_mid.tracks.append(new_track)

    nf = Path(f).parent.joinpath(Path(f).stem + '_dtx' + Path(f).suffix)
    print(f, '-->', nf)

    new_mid.save(nf)
