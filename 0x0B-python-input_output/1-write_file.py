#!/usr/bin/python3
'''
Module to write in_to file
'''


def write_file(filename="", text=""):
    ''' Writes some text to file '''
    with open(filename, 'w') as open_file:
        open_file.write(text)
        hold = open_file.tell()
    return hold

