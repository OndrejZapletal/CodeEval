# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 27/06/2016
# Description:
""" Unit tests for lights_out application. """

import unittest

from lights_out import print_grid, grid, parse_line


class MainTest(unittest.TestCase):

    """ Docstring """

    # @classmethod
    # def setUp(cls):
    #     """Test Set Up"""
    #     pass

    # @classmethod
    # def tearDown(cls):
    #     """Test Clean Up"""
    #     pass

    def test_lights_out(self):
        """ Docstring """
        data = ["00", ".."]
        result = print_grid(data)
        result_correct = " |12\n----\n1|00\n2|..\n"
        self.assertEqual(result, result_correct)

    def test_grid_object(self):
        """ Test of creataion of grid object. """
        new_grid = grid(2, 2, [])
        result = print_grid(new_grid)
        result_correct = " |12\n----\n1|..\n2|..\n"
        self.assertEqual(result, result_correct)

    def test_parse_line(self):
        self.assertEqual(parse_line("2 2 ..|OO"), [2, 2, [[1, 0], [1, 1]]])

    def test_valid_index1(self):
        self.assertEqual(grid(2, 2, [])._valid_index(0, 0), True)

    def test_valid_index2(self):
        self.assertEqual(grid(2, 2, [])._valid_index(1, 1), True)

    def test_valid_index3(self):
        self.assertEqual(grid(2, 2, [])._valid_index(2, 2), False)

    def test_valid_index4(self):
        self.assertEqual(grid(2, 2, [])._valid_index(0, 2), False)
