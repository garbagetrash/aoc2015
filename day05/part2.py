#!/usr/bin/python
import sys


def func1(in_file):
    with open(in_file) as f:
        string_list = list(map(lambda x: x.strip(), f.readlines()))
        good_cnt = 0
        for s in string_list:
            # Now check for double character with 1 character in between
            good = False
            for i in range(len(s) - 2):
                if s[i] == s[i + 2]:
                    good = True
            if not good:
                continue

            # Check for pairs of two letter substrings
            good = False
            for i in range(len(s) - 3):
                pair = str(s[i] + s[i + 1])
                remaining = s[i + 2:]
                if pair in remaining:
                    good = True
            if not good:
                continue

            good_cnt += 1

    return good_cnt


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
