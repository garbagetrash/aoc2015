#!/usr/bin/python
import sys


def houses_with_at_least_one(dir_file):
    with open(dir_file) as f:
        directions = f.read()

    santa = (0, 0)
    robo = (0, 0)
    visited = {santa: 2}
    for i, c in enumerate(directions):
        # Decide who is being dispatched
        if i % 2 == 0:
            active = santa
        else:
            active = robo

        # Send them to new location
        if c == "^":
            active = (active[0] + 1, active[1])
        elif c == "v":
            active = (active[0] - 1, active[1])
        elif c == "<":
            active = (active[0], active[1] - 1)
        elif c == ">":
            active = (active[0], active[1] + 1)

        # Update santa or robo position
        if i % 2 == 0:
            santa = active
        else:
            robo = active

        # Update dictionary of results
        if active not in visited:
            visited[active] = 1
        else:
            visited[active] += 1

    return len(visited)


if __name__ == '__main__':
    num_houses = houses_with_at_least_one(sys.argv[1])
    print('Number of houses with at least one visit: {}'.format(num_houses))
