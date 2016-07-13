# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 13/07/2016
# Description:
""" n_mode_m application. """
import sys


def modulo(string):
    [n, m] = string.split(',')
    n = int(n)
    m = int(m)
    while n >= 0:
        n -= m
    return n + m


def main():
    """ TODO: main function description."""
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            if test[-1] == '\n':
                test = test[:-1]
            if test != "":
                print(modulo(test))

if __name__ == "__main__":
    main()
