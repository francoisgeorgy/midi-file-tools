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
