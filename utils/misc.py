# coding=utf-8

from pathlib import Path


def suffixFilename(filename, suffix):
    return Path(filename).parent.joinpath(Path(filename).stem + suffix + Path(filename).suffix)
