#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) not in (int, float):
    raise TypeError()
    if type(b) not in (int, float):
    raise TypeError()
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
