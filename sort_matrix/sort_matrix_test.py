# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 12/07/2016
# Description:
""" Unit tests for sort_matrix application. """

import unittest
from collections import namedtuple
from sort_matrix import find_equal

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
