import sys


def find_sort_indexes(number_list):
    index_number_list = []
    for i, item in enumerate(number_list):
        index_number_list.append([item, i])
    index_number_list = sorted(index_number_list, key=lambda x: x[0])
    sorted_indexes = []
    for item in index_number_list:
        sorted_indexes.append(item[1])
    return sorted_indexes


def sort_matrix(matrix, sorted_indexes):
    new_matrix = []
    for row in matrix:
        new_row = []
        for index in sorted_indexes:
            new_row.append(row[index])
        new_matrix.append(new_row)
    return new_matrix


def extract_matrix(string):
    matrix = []
    rows = string.split('|')
    for row in rows:
        matrix.append(row.split())
    return matrix


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test[-1] == '\n':
            test = test[:-1]
        if test:
            matrix = extract_matrix(test)
            print(matrix)
            indexes = find_sort_indexes(matrix[0])
            matrix = sort_matrix(matrix, indexes)
            print(matrix)
