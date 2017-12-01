#!/usr/bin/python
import sys


def end_floor(in_file):

    with open(in_file) as f:
        s = f.read().strip()

    floor = 0
    pos = 0
    for c in s:
        pos += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    return floor


if __name__ == '__main__':
    floor = end_floor(sys.argv[1])
    print('Final floor: {}\n'.format(floor))
