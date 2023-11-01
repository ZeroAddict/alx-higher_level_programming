#!/usr/bin/python3
"""Module for the functn say_my_name mthd"""

def say_my_name(first_name, last_name):
    """Method for say_my_name to print 1st n last name.
    Args:
        first_name: first name
        last_name: last name
    Raises:
        TypeError: raised if first and last names are not strings
    """
    if type(first_name) not in (str): 
        raise TypeError('first_name must be a string')
    if type(last_name) not in (str):
        raise TypeError('last_name must be a string')
    print("My name is {.s} {.s})".format{first_name, last_name})

if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
