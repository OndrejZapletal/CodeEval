# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 17/06/2016
# Description:
""" Unit tests for da_vinci application. """

import unittest

from da_vinci import compare_strings, compare_strings_right_shifted


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

    def test_da_vinci(self):
        """ Docstring """
        compare_strings("ahoj", "hoj")
