#!/usr/bin/python
import sys


def box_area(dim):
    # TODO: This
    s1 = dim[0] * dim[1]
    s2 = dim[1] * dim[2]
    s3 = dim[0] * dim[2]

    min_val = min(s1, s2)
    min_val = min(s3, min_val)

    return 2 * s1 + 2 * s2 + 2 * s3 + min_val


def get_total_wrapping_paper(box_dim_file):
    box_dim_list = []
    with open(box_dim_file) as f:
        box_dims = f.readlines()
        for dim in box_dims:
            box_dim_list.append(list(map(lambda z: int(z), dim.strip().split('x'))))

    # Given box_dim_list, calculate square footage per dim in the list
    total_area = 0
    for dim in box_dim_list:
        total_area += box_area(dim)

    return total_area


if __name__ == '__main__':
    total = get_total_wrapping_paper(sys.argv[1])
    print('Total area: {}'.format(total))
