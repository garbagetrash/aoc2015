#!/usr/bin/python
import sys


def houses_with_at_least_one(dir_file):
    with open(dir_file) as f:
        directions = f.read()

    return 0


if __name__ == '__main__':
    num_houses = houses_with_at_least_one(sys.argv[1])
