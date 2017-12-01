#!/usr/bin/python
import sys


signals = {}


def parse_arg(arg):
    try:
        return int(signals[arg])
    except KeyError:
        try:
            return int(arg)
        except ValueError:
            raise Exception('WTF')


def parse_line(instr):
    try:
        if instr.split()[-1] in signals:
            return True
        if 'OR' in instr:
            instr = instr.split()
            s1 = parse_arg(instr[0])
            s2 = parse_arg(instr[2])
            signals[instr[-1]] = s1 | s2
        elif 'AND' in instr:
            instr = instr.split()
            s1 = parse_arg(instr[0])
            s2 = parse_arg(instr[2])
            signals[instr[-1]] = s1 & s2
        elif 'LSHIFT' in instr:
            instr = instr.split()
            s1 = parse_arg(instr[0])
            s2 = parse_arg(instr[2])
            signals[instr[-1]] = s1 * (2 ** s2)
        elif 'RSHIFT' in instr:
            instr = instr.split()
            s1 = parse_arg(instr[0])
            s2 = parse_arg(instr[2])
            signals[instr[-1]] = s1 / (2 ** s2)
        elif 'NOT' in instr:
            instr = instr.split()
            s1 = parse_arg(instr[1])
            signals[instr[-1]] = ~s1
        else:
            instr = instr.split()
            s1 = parse_arg(instr[0])
            signals[instr[-1]] = s1
    except Exception:
        return False

    return True


def construct_circuit(in_file):
    with open(in_file) as f:
        instr_list = list(map(lambda x: x.strip(), f.readlines()))
        processed = [False] * len(instr_list)
        while not all(processed):
            for i in range(len(instr_list)):
                if not processed[i]:
                    processed[i] = parse_line(instr_list[i])

    return signals['a']


if __name__ == '__main__':
    construct_circuit(sys.argv[1])
    temp = signals['a']
    signals = {}
    signals['b'] = temp
    output = construct_circuit(sys.argv[1])
    print('Output: {}'.format(output))
