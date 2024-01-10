#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i]))

''' OR
def print_sorted_dictionary(a_dictionary):
    for key, val in sorted(a_dictionary.items()):
        print("{:s}: {}".format(key, val))
'''
