# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 12/07/2016
# Description:
""" Unit tests for sort_matrix application. """

import unittest
from collections import namedtuple
from sort_matrix import find_equal, update_matrix, get_matrix_subset, find_sort_indexes

Index = namedtuple('Index', 'x1 x2')


class MainTest(unittest.TestCase):

    """ Docstring """

    @classmethod
    def setUp(cls):
        """Test Set Up"""
        pass

    @classmethod
    def tearDown(cls):
        """Test Clean Up"""
        pass

    def test_sort_matrix_1(self):
        """ Docstring """
        matrix = [[0, 4, 4, 0]]
        result = find_equal(matrix)
        self.assertEqual(result, [Index(x1=1, x2=2)])

    def test_sort_matrix_2(self):
        """ Docstring """
        matrix = [[4, 4, 4, 4]]
        result = find_equal(matrix)
        self.assertEqual(result, [Index(x1=0, x2=3)])

    def test_sort_matrix_3(self):
        """ Docstring """
        matrix = [[4, 4, 4, 0]]
        result = find_equal(matrix)
        self.assertEqual(result, [Index(x1=0, x2=2)])

    def test_sort_matrix_4(self):
        """ Docstring """
        matrix = [[4, 3, 4, 0]]
        result = find_equal(matrix)
        self.assertEqual(result, [])

    def test_sort_matrix_5(self):
        """ Docstring """
        matrix = [[4, 3, 3, 4, 4, 0]]
        result = find_equal(matrix)
        self.assertEqual(result, [Index(x1=1, x2=2), Index(x1=3, x2=4)])

    def test_update_matrix_1(self):
        """ Docstring """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        submatrix = [[0, 0], [0, 0]]
        result = update_matrix(matrix, submatrix, Index(x1=1, x2=3))
        self.assertEqual(result, [[1, 2, 3], [4, 0, 0], [7, 0, 0]])

    def test_update_matrix_2(self):
        """ Docstring """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        submatrix = [[0, 0, 0], [0, 0, 0]]
        result = update_matrix(matrix, submatrix, Index(x1=0, x2=3))
        self.assertEqual(result, [[1, 2, 3], [0, 0, 0], [0, 0, 0]])

    def test_update_matrix_3(self):
        """ Docstring """
        matrix = [[1, 2], [3, 4]]
        submatrix = [[0, 0], ]
        result = update_matrix(matrix, submatrix, Index(x1=0, x2=1))
        self.assertEqual(result, [[1, 2], [0, 0]])

    def test_get_matrix_subset_1(self):
        """ Docstring """
        matrix = [[4, 3], [4, 0]]
        result = get_matrix_subset(matrix, Index(x1=0, x2=0))
        self.assertEqual(result, [[4]])

    def test_get_matrix_subset_2(self):
        """ Docstring """
        matrix = [[4, 3, 1], [4, 1, 3], [4, 3, 2]]
        result = get_matrix_subset(matrix, Index(x1=1, x2=3))
        self.assertEqual(result, [[1, 3], [3, 2]])

    def test_find_sort_indexes_1(self):
        """ Docstring """
        matrix = [44, 8]
        result = find_sort_indexes(matrix)
        self.assertEqual(result, [1, 0])
