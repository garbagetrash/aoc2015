#!/usr/bin/python
import sys
import hashlib


def find_num(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()

    num = 1
    while True:
        h = hashlib.md5((in_string + str(num)).encode('utf-8')).hexdigest()
        if h[:6] == '000000':
            return num
        else:
            num += 1


if __name__ == '__main__':
    output = find_num(sys.argv[1])
    print('Output: {}'.format(output))
