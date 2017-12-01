#!/usr/bin/python
import sys


def func1(in_file):
    with open(in_file) as f:
        string_list = list(map(lambda x: x.strip(), f.readlines()))
        good_cnt = 0
        for s in string_list:
            # First check for bad substrings
            if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
                continue

            # Now check for double character
            good = False
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    good = True
            if not good:
                continue

            # Now check for at least 3 vowels
            cnt = 0
            for c in s:
                if c in 'aeiou':
                    cnt += 1
            if cnt < 3:
                continue

            good_cnt += 1

    return good_cnt


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
