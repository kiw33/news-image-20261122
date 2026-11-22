#!/usr/bin/env python3
"""Entrypoint for the news-image-20261122 entry.

The picture itself ships in this repository as entry.png (rendered by
draw_news22.py). All this program does is place a copy of it where the
grader expects the result, so repeated runs write identical bytes.

Standard library only: no Pillow, no network, no writes outside the
output directory. Python 3.13.
"""

import os
import shutil
import sys

IMAGE = "entry.png"


def pick_output_dir():
    """Where the grader wants the image.

    MAKEFUN_OUTPUT_DIR first, then the sandbox default /output, then a
    local out/ folder next to this file when run by hand.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE)
    if not os.path.isfile(source):
        print("missing {} — run draw_news22.py first".format(source), file=sys.stderr)
        return 1
    size = os.path.getsize(source)
    if size == 0:
        print("empty {} — regenerate it with draw_news22.py".format(source), file=sys.stderr)
        return 1
    out_dir = pick_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, IMAGE)
    shutil.copyfile(source, target)
    copied = os.path.getsize(target)
    if copied != size:
        print("copy mismatch: {} is {} bytes, expected {}".format(target, copied, size), file=sys.stderr)
        return 1
    print("wrote {} ({} bytes)".format(target, copied))
    return 0


if __name__ == "__main__":
    sys.exit(main())
