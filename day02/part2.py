#!/usr/bin/python
import sys


def ribbon_length(dim):
    perimeter = 2 * dim[0] + 2 * dim[1]
    bow = dim[0] * dim[1] * dim[2]

    return perimeter + bow


def box_area(dim):
    s1 = dim[0] * dim[1]
    s2 = dim[1] * dim[2]
    s3 = dim[0] * dim[2]

    return 3 * s1 + 2 * s2 + 2 * s3


def get_totals(box_dim_file):
    box_dim_list = []
    with open(box_dim_file) as f:
        box_dims = f.readlines()
        for dim in box_dims:
            box_dim_list.append(sorted(list(map(lambda z: int(z), dim.strip().split('x')))))

    total_area = 0
    total_length = 0
    for dim in box_dim_list:
        total_area += box_area(dim)
        total_length += ribbon_length(dim)

    return total_area, total_length


if __name__ == '__main__':
    total_area, total_length = get_totals(sys.argv[1])
    print('Total area: {}'.format(total_area))
    print('Total ribbon length: {}'.format(total_length))
