#!/usr/bin/python
import sys


def count_floors(s):
    up_cnt = 0
    down_cnt = 0
    for c in s:
        if c == '(':
            up_cnt += 1
        elif c == ')':
            down_cnt += 1

    return up_cnt, down_cnt


if __name__ == '__main__':
    up_cnt, down_cnt = count_floors(sys.argv[1])
    print('Up Count: {}\nDown Count: {}\nEnd Floor: {}\n'.format(
        up_cnt, down_cnt, up_cnt - down_cnt))
