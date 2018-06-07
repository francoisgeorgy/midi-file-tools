#!/usr/bin/env python3
# coding=utf-8

import argparse
import mido
# from mido import MetaMessage

mid = mido.MidiFile(type=0) # single track  VERY IMPORTANT for XF

track = mido.MidiTrack()

track.name = "Test XF 11"

track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8))

track.append(mido.MetaMessage('set_tempo', tempo=322580))

# XF Version ID
track.append(mido.MetaMessage('sequencer_specific', data=[0x43, 0x7B, 0, 0x58, 70, 48, 50, 0, 1]))


# track.append(mido.Message('sysex', data=[0x7E, 0x7F, 9, 1]))
# track.append(mido.MetaMessage('sequencer_specific', data=[0x43, 0x7B, 0x24, 0x60]))

# track.append(mido.MetaMessage('copyright', text='(P) 2011 Yamaha Corporation'))

track.append(mido.MetaMessage('text', text='XFln:L1:Xest TF 111:Composer:::AARTIST:'))

# track.append(mido.Message('sysex', data=[0x43, 0x10, 0x4C, 0, 0, 0x7E, 0]))
# track.append(mido.MetaMessage('sequencer_specific', data=[0x43, 0x7B, 16, 32, 0, 0, 64, 59, 55, 50, 45, 40]))

track.append(mido.Message('note_on', channel=10, note=36, velocity=64, time=10))
track.append(mido.Message('note_off', channel=10, note=36, velocity=64, time=10))
track.append(mido.Message('note_on', channel=10, note=38, velocity=64, time=20))
track.append(mido.Message('note_off', channel=10, note=38, velocity=64, time=20))

# track.append(mido.Message('sysex', data=[0x7E,0x7F,9,1]))


mid.tracks.append(track)

mid.save('test_xf.mid')
