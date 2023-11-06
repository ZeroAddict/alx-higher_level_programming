#!/usr/bin/python3

"""
module for BasevGeometry.
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raisigm an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate class functn"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
