#!/usr/bin/python3
'''
Module to read & print contents of file
'''


def read_file(filename=""):
    ''' Reads file and prints contents '''
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
