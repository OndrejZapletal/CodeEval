# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 12/07/2016
# Description:
""" code_combinations application. """

import sys


def extract_matrix(string):
    matrix = []
    rows = string.split('|')
    for row in rows:
        matrix.append(list(row.strip()))
    return matrix


def find_code(matrix):
    code_found = 0
    for i, line in enumerate(matrix[:-1]):
        for n, _ in enumerate(line[:-1]):
            if check_for_combination(matrix, i, n):
                code_found += 1
    return code_found


def check_for_combination(matrix, x, y):
    new_matrix = []
    new_matrix.append(matrix[x][y])
    new_matrix.append(matrix[x+1][y])
    new_matrix.append(matrix[x][y+1])
    new_matrix.append(matrix[x+1][y+1])
    return 'c' in new_matrix and 'o' in new_matrix and 'd' in new_matrix and 'e' in new_matrix


def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            if test[-1] == '\n':
                test = test[:-1]
            if test:
                matrix = extract_matrix(test)
                result = find_code(matrix)
                print("%s" % str(result))


if __name__ == "__main__":
    main()
