#!/usr/bin/python
import sys


signals = {}


def parse_line(instr):
    try:
        if 'OR' in instr:
            instr = instr.split()
            signals[instr[-1]] = int(signals[instr[0]]) ^ int(signals[instr[2]])
        elif 'AND' in instr:
            instr = instr.split()
            signals[instr[-1]] = int(signals[instr[0]]) & int(signals[instr[2]])
        elif 'LSHIFT' in instr:
            instr = instr.split()
            signals[instr[-1]] = int(signals[instr[0]]) * (2 ** int(instr[2]))
        elif 'RSHIFT' in instr:
            instr = instr.split()
            signals[instr[-1]] = int(signals[instr[0]]) / (2 ** int(instr[2]))
        elif 'NOT' in instr:
            instr = instr.split()
            signals[instr[-1]] = ~int(signals[instr[1]])
        else:
            instr = instr.split()
            if instr[0] in signals:
                signals[instr[-1]] = signals[instr[0]]
            else:
                signals[instr[-1]] = int(instr[0])
    except KeyError:
        return


def construct_circuit(in_file):
    with open(in_file) as f:
        instr_list = list(map(lambda x: x.strip(), f.readlines()))
        processed = [False] * len(instr_list)
        while not all(processed):
            for i in range(len(instr_list)):
                if not processed[i]:
                    parse_line(instr_list[i])
                    processed[i] = True

    return signals['a'].value()


if __name__ == '__main__':
    output = construct_circuit(sys.argv[1])
    print('Output: {}'.format(output))
