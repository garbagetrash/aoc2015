#!/usr/bin/python
import sys
import numpy as np


lights = np.zeros((1000, 1000))


def get_coords(instr):
    clist = []
    for w in instr:
        if ',' in w:
            clist.append(list(map(lambda x: int(x), w.split(','))))
    if len(clist) != 2:
        raise ValueError('Did not find 2 coords in {}'.format(instr.join()))
    return clist[0], clist[1]


def parse_line(instr):
    instr = instr.split()
    c1, c2 = get_coords(instr)
    if instr[0] == 'toggle':
        # brightness += 2
        lights[c1[0]:c2[0]+1, c1[1]:c2[1]+1] += 2
    elif instr[1] == 'on':
        # Turn lights on
        lights[c1[0]:c2[0]+1, c1[1]:c2[1]+1] += 1
    else:
        # Turn lights off
        lights[c1[0]:c2[0]+1, c1[1]:c2[1]+1] -= 1
        lights[lights<0] = 0


def setup_lights(in_file):
    with open(in_file) as f:
        instr_list = list(map(lambda x: x.strip(), f.readlines()))
        for instr in instr_list:
            parse_line(instr)


if __name__ == '__main__':
    setup_lights(sys.argv[1])
    print('Output: {}'.format(np.sum(lights)))
