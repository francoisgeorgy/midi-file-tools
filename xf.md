
ff 7f 09 43 7b 00 58 46 30 32 00 03
                  88 70

s1 = 00
s2 = 03

00000000 000kl0si
00000000 00000011

‘XF02’(58 46 30 32) s1,s0 Status
Version 2.0
00000000 000kl0si
Each bit is a flag indicating the presence (1) or absence (0) of the corresponding data/chunk
i: XF Information Header / XF Information Header Chunk 
l: Lyric Meta-Event
k: XF Karaoke Message / XF Karaoke Message Chunk
s: XF Style Message




4d 54 68 64 00 00 00 06 00 01 00 01 01 e0 4d 54
M  T  h  d                 ^^
            
length 00 00 00 06
format 00 01            
                            
"MThd" 4 bytes
the literal string MThd, or in hexadecimal notation: 0x4d546864. These four characters at the start of the MIDI file indicate that this is a MIDI file.
<header_length> 4 bytes
length of the header chunk (always 6 bytes long--the size of the next three fields which are considered the header chunk).
<format> 2 bytes
0 = single track file format 
1 = multiple track file format 
2 = multiple song file format (i.e., a series of type 0 files)
<n> 2 bytes
number of track chunks that follow the header chunk
<division> 2 bytes
unit of time for delta timing. If the value is positive, then it represents the units per beat. For example, +96 would mean 96 ticks per beat. If the value is negative, delta times are in SMPTE compatible units.
                             
                             
                             
                             
                             
                             
         $ ./midi-merge-tracks.py tmp/_\ Verse-1.mid
         {'type': 'track_name', 'name': '_ Verset no 1', 'time': 0}
         {'type': 'time_signature', 'numerator': 4, 'denominator': 4, 'clocks_per_click': 24, 'notated_32nd_notes_per_beat': 8, 'time': 0}
         {'type': 'set_tempo', 'tempo': 571428, 'time': 0}
         {'type': 'time_signature', 'numerator': 4, 'denominator': 4, 'clocks_per_click': 24, 'notated_32nd_notes_per_beat': 8, 'time': 0}
         {'type': 'end_of_track', 'time': 0}

