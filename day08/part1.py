#!/usr/bin/python
import sys


def count_chars(line):
    return len(line)


def count_string_chars(line):
    cnt = 0
    i = 0
    while i < len(line):
        if line[i] == '\\':
            if line[i + 1] == 'x':
                cnt += 1
                i += 3
            else:
                cnt += 1
                i += 1
        elif line[i] != '"':
            cnt += 1

        i += 1

    return cnt


def chars_less_str(in_file):
    with open(in_file) as f:
        s_list = list(map(lambda x: x.strip(), f.readlines()))
        mem_chars = 0
        chars = 0
        for line in s_list:
            mem_chars += count_chars(line)
            chars += count_string_chars(line)

    return mem_chars - chars


if __name__ == '__main__':
    output = chars_less_str(sys.argv[1])
    print('Output: {}'.format(output))
