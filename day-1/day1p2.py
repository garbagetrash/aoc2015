#!/usr/bin/python
import sys


def count_floors(s):
    floor = 0
    pos = 0
    for c in s:
        pos += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
            if floor <= -1:
                return pos


if __name__ == '__main__':
    pos = count_floors(sys.argv[1])
    print('First position in basement: {}\n'.format(pos))
