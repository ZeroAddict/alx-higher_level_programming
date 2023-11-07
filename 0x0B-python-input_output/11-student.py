#!/usr/bin/python3
"""
Module for Class Student.
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialize Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary to JSON file """
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ret = {}
            for x, r in self.__dict__.items():
                if x in attrs:
                    ret[x] = r
            return ret
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Change att"""
        for x, r in json.items():
            self.__dict__[x] = r
