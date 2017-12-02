#!/usr/bin/python
import sys
import itertools


dists = {}
locations = []


def parse_line(line):
    larr = line.split()
    dists[(larr[0], larr[2])] = int(larr[4])
    if larr[0] not in locations:
        locations.append(larr[0])
    if larr[2] not in locations:
        locations.append(larr[2])


def func1(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))
        for line in str_list:
            parse_line(line)

        total_arr = []
        paths = list(itertools.permutations(locations))
        for path in paths:
            total = 0
            for i in range(len(path) - 1):
                if (path[i], path[i + 1]) in dists:
                    total += dists[(path[i], path[i + 1])]
                else:
                    total += dists[(path[i + 1], path[i])]

            total_arr.append(total)

    return min(total_arr)


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
