# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 12/07/2016
# Description:
""" sort_matrix application. """

from collections import namedtuple
import sys

Index = namedtuple('Index', 'x1 x2')

def extract_matrix(string):
    matrix = []
    rows = string.split('|')
    for row in rows:
        number_row = []
        for item in row.split():
            number_row.append(int(item))
        matrix.append(number_row)
    return matrix


def sort_matrix(matrix):
    new_matrix = sort_columns(matrix)
    duplicit_indexes_list = find_equal(new_matrix)

    if duplicit_indexes_list:
        for duplicit_indexes in duplicit_indexes_list:

            matrix_subset = get_matrix_subset(new_matrix, duplicit_indexes)
            matrix_subset_sorted = sort_matrix(matrix_subset)
            new_matrix_updated = update_matrix(new_matrix, matrix_subset_sorted, duplicit_indexes)

        return new_matrix_updated
    return new_matrix


def sort_columns(matrix):
    sorted_indexes = find_sort_indexes(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        for index in sorted_indexes:
            new_row.append(row[index])
        new_matrix.append(new_row)
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


def find_sort_indexes(number_list):
    index_number_list = []
    for i, item in enumerate(number_list):
        index_number_list.append([item, i])
    index_number_list = sorted(index_number_list, key=lambda x: x[0])
    sorted_indexes = []
    for item in index_number_list:
        sorted_indexes.append(item[1])
    return sorted_indexes


def get_matrix_subset(matrix, indexes):
    new_matrix = []
    for line in matrix[1:]:
        line_to_add = line[indexes.x1:indexes.x2+1]
        new_matrix.append(line_to_add)
    return new_matrix


def update_matrix(matrix, matrix_subset, indexes):
    new_matrix = list(matrix)
    for i, line in enumerate(matrix[1:]):
        for n, item in enumerate(line[indexes.x1:indexes.x2+1]):
            new_matrix[i+1][n+indexes.x1] = matrix_subset[i][n]
    return new_matrix


def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            if test[-1] == '\n':
                test = test[:-1]
            if test:
                matrix = extract_matrix(test)
                matrix = sort_matrix(matrix)
                line_result = ""
                for line in matrix:
                    item_result = ""
                    for item in line:
                        item_result += " " + str(item)
                    line_result += " " +  item_result.strip() + " |"
                print(line_result[:-1].strip())


if __name__ == "__main__":
    main()
