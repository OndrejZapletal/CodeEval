# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 13/07/2016
# Description:
""" mixed_content application. """
import sys


def convert_string(string):
    alpha_string  = ""
    digit_string  = ""

    for word in string.split(','):
        if word.isalpha():
            alpha_string += word + ','
        else:
            digit_string += word + ','

    if not alpha_string:
        return string
    elif not digit_string:
        return string
    else:
        return alpha_string[:-1] + '|' + digit_string[:-1]


def main():
    """ TODO: main function description."""
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            if test[-1] == '\n':
                test = test[:-1]
            if test != "":

                print(convert_string(test))

if __name__ == "__main__":
    main()
