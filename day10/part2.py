#!/usr/bin/python
import sys


def one_iter(seq):
    output = ''
    i = 0
    while i < len(seq):
        cnt = 1
        try:
            while seq[i] == seq[i + cnt]:
                cnt += 1
        except IndexError:
            pass

        output += str(cnt) + seq[i]
        i += cnt

    return output


def look_and_say(in_file, n_times):
    with open(in_file) as f:
        seq = f.read().strip()
        for i in range(n_times):
            seq = one_iter(seq)

    return len(seq)


if __name__ == '__main__':
    output = look_and_say(sys.argv[1], 50)
    print('Output: {}'.format(output))
