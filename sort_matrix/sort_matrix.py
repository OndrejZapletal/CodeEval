# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 12/07/2016
# Description:
""" sort_matrix_columns application. """

from collections import namedtuple
import ipdb

Index = namedtuple('Index', 'x1 x2')


def update_matrix(matrix, matrix_subset, indexes):
    new_matrix = list(matrix)
    for i, line in enumerate(matrix[1:]):
        for n, item in enumerate(line[indexes.x1:indexes.x2]):
            new_matrix[i][n] = matrix_subset[i-1][n-indexes.x1]
    return new_matrix


def get_matrix_subset(matrix, indexes):
    new_matrix = []
    for line in matrix[1:]:
        new_matrix.append(line[indexes.x1:indexes.x2])
    return new_matrix


def find_equal(matrix):
    """ Done """
    duplicit_indexes_list = []
    found = False
    previous = None
    x = None
    for i, item in enumerate(matrix[0]):
        if not found:
            if previous == item:
                found = True
                x = i - 1
                if i == len(matrix[0])-1:
                    duplicit_indexes_list.append(Index(x1=x, x2=i))
        else:
            if previous != item:
                duplicit_indexes_list.append(Index(x1=x, x2=i-1))
                found = False
            else:
                if i == len(matrix[0])-1:
                    duplicit_indexes_list.append(Index(x1=x, x2=i))
        previous = item
    return duplicit_indexes_list


def sort_columns(matrix):
    pass


def sort_matrix_columns(matrix):
        matrix = sort_columns(matrix)
        duplicit_indexes_list = find_equal(matrix)
        if duplicit_indexes_list:
            for duplicit_indexes in duplicit_indexes_list:
                matrix_subset = get_matrix_subset(matrix, duplicit_indexes)
                matrix_subset_sorted = sort_matrix_columns(matrix_subset)
                matrix = update_matrix(matrix, matrix_subset_sorted, duplicit_indexes)


def main():
    """ TODO: main function description."""
    matrix = [[0, 4, 4], [3, 3, 3], [3, 3, 3]]
    print(find_equal(matrix))


if __name__ == "__main__":
    main()
