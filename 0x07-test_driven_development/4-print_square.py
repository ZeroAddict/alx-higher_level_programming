#!/usr/bin/python3
"""Module: print_square methd"""
def print_square(size):
    """Method for print_square to print sq of size size.
    Args:
        first_name: square size
    Raises:
        TypeError: raised if size is not int
        ValueError: raised if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
