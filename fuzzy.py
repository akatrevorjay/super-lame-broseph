#!/usr/bin/env python

from __future__ import print_function
import sys


def run(start='', idx=0, tokens=None):
    """ Takes input in the form of newlines, where each contain whitespace-delimited
    permutations. These permutations are then yielded. Use "" or '' to signify optional.
    """
    if tokens is None:
        with open(sys.stdin, 'r') as fh:
            tokens = [x.split() for x in fh.readlines()]

    for x in tokens[idx]:
        if x in ["''", '""']:
            cur = start
        else:
            cur = '%s%s' % (start, x)
            yield cur
        if idx + 1 != len(tokens):
            for y in run(cur, idx+1, tokens):
                yield y


for password in run():
    print('%s\n' % password)

