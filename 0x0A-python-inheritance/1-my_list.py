#!/usr/bin/python3
"""
module for MyList
"""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Print list sorted."""
        print(sorted(self))
