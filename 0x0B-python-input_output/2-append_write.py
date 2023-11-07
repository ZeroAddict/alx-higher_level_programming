#!/usr/bin/python3
'''
Module to append text to file
'''


def append_write(filename="", text=""):
    ''' Appends txt to file '''
    with open(filename, 'a') as open_file:
        hold = open_file.write(text)
    return hold
