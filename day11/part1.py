#!/usr/bin/python
import sys


straights = []
letters = []


def check_password(password):
    nums = list(map(lambda x: ord(x), password))
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i] - nums[i + 1])
    if diffs.count(0) >= 2:
        if diffs[diffs.index(0) + 1] != 0:
            pass
        else:
            return False
    else:
        return False
    if diffs.count(1) >= 2:
        if diffs[diffs.index(1) + 1] == 1:
            pass
        else:
            return False
    return True


def build_local_solution_set(prior):
    sset = []
    for s in straights:
        for l1 in letters:
            for l2 in letters:
                sset.append(prior[:3] + [l1] + [l2] + s)
                sset.append(prior[:3] + [l1] + s + [l2])
                sset.append(prior[:3] + s + [l1] + [l2])

    sset.append(prior)
    sset = sorted(list(map(lambda x: ''.join(x), sset)))
    sset = list(set(filter(lambda x: check_password(x), sset)))
    sset.append(''.join(prior))
    sset = sorted(sset)

    idx = sset.index(''.join(prior))
    return sset[idx + 1]


def gen_letters():
    s = []
    i = 0
    for i in range(26):
        s.append(chr(ord('a') + i))

    s.remove('i')
    s.remove('o')
    s.remove('l')
    return s


def gen_straights():
    s = []
    for i in range(24):
        candidate = [chr(ord('a') + i), chr(ord('b') + i), chr(ord('c') + i)]
        if 'i' in candidate or 'o' in candidate or 'l' in candidate:
            pass
        else:
            s.append(candidate)

    return s


def password(in_file):

    with open(in_file) as f:
        password = [c for c in f.read().strip()]

        next_password = build_local_solution_set(password)

    return next_password


if __name__ == '__main__':
    letters = gen_letters()
    straights = gen_straights()
    output = password(sys.argv[1])
    print('Output: {}'.format(output))
