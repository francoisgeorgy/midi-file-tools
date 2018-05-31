# MIDI file tools

Requirements: 

- Python 3
- [Mido - MIDI Objects for Python](https://mido.readthedocs.io/en/latest/index.html)


## midi-dump

Dump (print) the content of a MIDI file.

    $ .midi-dump.py 105-Verse-1.mid 
    Track 0: 105 Verse 1
    <meta message track_name name='105 Verse 1' time=0>
    <meta message time_signature numerator=4 denominator=4 clocks_per_click=24 notated_32nd_notes_per_beat=8 time=0>
    <meta message set_tempo tempo=571428 time=0>
    <meta message time_signature numerator=4 denominator=4 clocks_per_click=24 notated_32nd_notes_per_beat=8 time=0>
    <meta message end_of_track time=0>
    Track 1: 105 Verse 1
    <meta message track_name name='105 Verse 1' time=0>
    note_on channel=9 note=49 velocity=111 time=0
    note_on channel=9 note=36 velocity=116 time=0
    ...
    note_on channel=9 note=36 velocity=60 time=48
    note_on channel=9 note=36 velocity=0 time=20
    <meta message end_of_track time=0>


## midi-trackname

Print the name of all tracks of a MIDI file.

    $ ./midi-trackname.py 105-Verse-1.mid 
    105 Verse 1
    105 Verse 1
    
    $ ./midi-trackname.py ../gm/*.mid
    ../gm/105-Chorus-1.mid: 105 Chorus 1
    ../gm/105-Chorus-1.mid: 105 Chorus 1
    ../gm/105-Verse-1.mid: 105 Verse 1
    ../gm/105-Verse-1.mid: 105 Verse 1

Change the name of all tracks of a MIDI file.

    $ ./midi-trackname.py Verse-1.mid -s "Verse 1"
    105 Verse 1 --> Verse 1
    105 Verse 1 --> Verse 1

## midi-notes

Print the list of notes found in the MIDI file.

    $ ./midi-notes.py pokerface.mid 
    28 Electric Guitar (clean)
    32 Guitar harmonics
    34 Electric Bass (finger)
    35 Electric Bass (pick)
    37 Slap Bass 1
    ...
    75 Recorder
    76 Pan Flute
    78 Shakuhachi
    80 Ocarina
    82 Lead 2 (sawtooth)
    83 Lead 3 (calliope)
    94 Pad 6 (metallic)

It is possible to choose the mapping for the notes names:

- `-m inst` for GM Level 1 Instruments
- `-m perc` for GM Level 1 Percussions


    $ ./midi-notes.py Verse-1.mid -m perc
    36 Bass Drum 1
    38 Acoustic Snare
    42 Closed Hi Hat
    49 Crash Cymbal 1

# TODO:

- midi-tracks : print the tracks used
- midi-channels : print the channels used; change the channels; for one track, for all tracks
- midi-transpose : transpose the notes for one channel; for all channels; for one track; for all tracks

