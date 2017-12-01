#!/usr/bin/python
import sys


def houses_with_at_least_one(dir_file):
    with open(dir_file) as f:
        directions = f.read()

    last = (0, 0)
    visited = {last: 1}
    for c in directions:
        if c == "^":
            last = (last[0] + 1, last[1])
        elif c == "v":
            last = (last[0] - 1, last[1])
        elif c == "<":
            last = (last[0], last[1] - 1)
        elif c == ">":
            last = (last[0], last[1] + 1)

        if last not in visited:
            visited[last] = 1
        else:
            visited[last] += 1

    return len(visited)


if __name__ == '__main__':
    num_houses = houses_with_at_least_one(sys.argv[1])
    print('Number of houses with at least one visit: {}'.format(num_houses))
