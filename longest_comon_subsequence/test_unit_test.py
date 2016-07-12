# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 2016-06-13
# Description:
""" Unit tests for the Longest Common Sequence. """

import unittest

from longest_common_sequence_pnr import find_common_letters, find_first_couples, not_larger
from longest_common_sequence_pnr import reminder_by_index, filter_unnecessary_couples
from longest_common_sequence_pnr import find_next_common
from longest_common_sequence_pnr import find_longest_common_string


class FindFirstCommonLetterTest(unittest.TestCase):

    def test_find_longest_common_string_1(self):
        result = find_longest_common_string("CGEPGYXFLNPGSVMVLVAEWM", "VUBGYJWTILLBVFZK")
        self.assertEqual(result, "GYLLV")

    def test_find_longest_common_string_2(self):
        result = find_longest_common_string("ABCVXA", "STXABC",)
        self.assertEqual(result, "ABC")


class FindNextCommonTest(unittest.TestCase):

    def test_find_next_common(self):
        new_list = []
        find_next_common("AB", "AB", "", new_list)
        self.assertEqual(new_list, ["AB", "A"])


class FindFirstCouplesTest(unittest.TestCase):

    def test_find_first_couples_1(self):
        letter_couples = [[0, 4], [3, 5], [3, 3], [0, 0]]
        result = find_first_couples(letter_couples)
        self.assertEqual(result, [[0, 0], [0, 0]])

    def test_find_first_couples_2(self):
        letter_couples = [[0, 4], [3, 5], [3, 3]]
        result = find_first_couples(letter_couples)
        self.assertEqual(result, [[0, 4], [3, 3]])

    def test_find_first_couples_3(self):
        letter_couples = [[0, 1], [3, 5], [3, 3]]
        result = find_first_couples(letter_couples)
        self.assertEqual(result, [[0, 1], [0, 1]])

    def test_find_first_couples_4(self):
        letter_couples = [[0, 1], [1, 0], [3, 3]]
        result = find_first_couples(letter_couples)
        self.assertEqual(result, [[0, 1], [1, 0]])


class FilterUnnecessaryCouples(unittest.TestCase):

    def test_filter_unnecessary_couples_1(self):
        result = filter_unnecessary_couples([[0, 4], [3, 5], [5, 6], [3, 3]])
        self.assertEqual(result, [[0, 4], [3, 3]])

    def test_filter_unnecessary_couples_2(self):
        result = filter_unnecessary_couples([[0, 4], [1, 1], [3, 5], [5, 6], [3, 3]])
        self.assertEqual(result, [[0, 4], [1, 1],  [3, 3]])


class NotLargerTest(unittest.TestCase):

    def test_not_larger_1(self):
        self.assertEqual(not_larger([0, 4], [5, 3]), True)

    def test_not_larger_2(self):
        self.assertEqual(not_larger([0, 3], [5, 3]), True)

    def test_not_larger_3(self):
        self.assertEqual(not_larger([5, 3], [0, 3]), False)


class ReminderByIndexTest(unittest.TestCase):

    def test_reminder_by_index_1(self):
        self.assertEqual(reminder_by_index("ABC", 0), "BC")

    def test_reminder_by_index_2(self):
        self.assertEqual(reminder_by_index("ABC", 1), "C")

    def test_reminder_by_index_3(self):
        self.assertEqual(reminder_by_index("ABC", 2), "")

    def test_reminder_by_index_4(self):
        self.assertEqual(reminder_by_index("ABC", 3), "")


class FindCommonLettersTest(unittest.TestCase):

    def test_find_common_letters_1(self):
        self.assertEqual(find_common_letters("ABC", "ABC"), [[0, 0], [1, 1], [2, 2]])

    def test_find_common_letters_2(self):
        self.assertEqual(find_common_letters("ABB", "ABC"), [[0, 0], [1, 1], [2, 1]])

    def test_find_common_letters_3(self):
        self.assertEqual(find_common_letters("ABC", "XYZ"), [])
