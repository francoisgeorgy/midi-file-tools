# coding=utf-8

import re


def clean_line(line):
    cl = line.strip()   #.rstrip('\n')
    if cl.isspace() or \
            cl.startswith('#') or \
            cl.startswith(';') or \
            cl.startswith('//') or \
            cl.startswith('--'):
        return None
    # Replace all runs of whitespace with a single dash
    return re.sub(r'\s+', ' ', cl)


def read_lines(file):
    """Generator function to read a file line by line.
    """
    with open(file) as f:
        line = f.readline()
        while line:
            cl = clean_line(line)
            if cl:
                yield cl
            line = f.readline()


def read_remap(file):
    remap = []
    for line in read_lines(file):
        parts = line.split(' ', 2)
        if parts[0] == parts[1]:
            continue    # ignore identity mapping
        try:
            remap.append({
                'from': int(parts[0]),
                'to': int(parts[1]),
                'comment': '' if len(parts) < 3 else parts[2]
            })
        except ValueError:
            print("ERROR: invalid value in '%s'" % line)
    return remap

# read a file describing a mapping between note numbers and notes names
def read_map(file):
    m = {}
    for line in read_lines(file):
        parts = line.split(' ', 1)
        try:
            m[int(parts[0])] = parts[1];
        except ValueError:
            print("ERROR: invalid value in '%s'" % line)

    return m
