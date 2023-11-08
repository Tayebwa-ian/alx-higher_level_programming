#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.items())
    for key, value in dic:
        print("{}: {}".format(key, value))
