# MIDI file tools

### Requirements:   

- Python 3
- [Mido - MIDI Objects for Python](https://mido.readthedocs.io/en/latest/index.html)


### Motivation:

These tools helps me convert MIDI files from ezDrummer to Yamaha DTX format. If they are useful for you, I'm happy :-) 


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

`-m inst` for GM Level 1 Instruments

`-m perc` for GM Level 1 Percussions

    $ ./midi-notes.py Verse-1.mid -m perc
    36 Bass Drum 1
    38 Acoustic Snare
    42 Closed Hi Hat
    49 Crash Cymbal 1


## midi-remap

Change note numbers according to a provided _map_.

This tool also provides the possibility to change the channel of the remapped notes.

This is especially useful for MIDI drum tracks where, often, the drum notes and channel do not respect the GM standard. 

    $ ./midi-remap.py maps/test-map file01.mid -c 10


# TODO:

- midi-tracks : print the tracks used; delete a track; copy a track with another channel
- midi-channels : print the channels used; change the channels; for one track, for all tracks
- midi-transpose : transpose the notes for one channel; for all channels; for one track; for all tracks
    - transpose by a fixed number of semitones
    - transpose by an interval (alias of number of semitones)
    - transpose by an interval, according to a scale and a root (e.g. will correctly choose major 3rd or minor 3rd)
- midi-double: double the notes with the same possibilities as for the transposition
- midi-chords: change notes to chords, according to a scale and a root


## instrument map file format

A map if a file containing one or more lines defining a name for a specific MIDI note number.

    <NOTE-NUMBER> <INSTRUMENT-NAME>
    
- NOTE-NUMBER must be a number between 0 and 127
- INSTRUMENT-NAME is a string.

Parsing rules:

- A _blank space_ is defined as a serie of one or more space character or tab character. The two can be mixed.
- Any blank space at the beginning or at the end of the line will be removed.
- Lines that begin with `//`, `--`, `;` or `#` are comments and will be ignored.
- Empty lines will be ignored. 
- The first blank space is the separator between NOTE-NUMBER and INSTRUMENT-NAME.
- INSTRUMENT-NAME can includes blank spaces.
- If INSTRUMENT-NAME begins and ends with double quotes, the double quotes will be removed.
- Any other lines that do not begin with a number will generate an error and the parsing will stop.

## remapping file format

A re-mapping file is a file containing one or more lines defining a mapping from one MIDI note number to another MIDI note number
                      
    <FROM-NOTE-NUMBER> <TO-NOTE-NUMBER> <OPTIONAL-COMMENT>
                          
- FROM-NOTE-NUMBER must be a number between 0 and 127
- TO-NOTE-NUMBER must be a number between 0 and 127
- OPTIONAL-COMMENT can be anything. Use it to document the mapping.

Parsing rules:

The parsing rules are the same as for the instrument map file, with the following changes:

- The first blank space is the separator between FROM-NOTE-NUMBER and TO-NOTE-NUMBER.
- The second blank space marks the end of TO-NOTE-NUMBER and anything after it is ignored.
 
