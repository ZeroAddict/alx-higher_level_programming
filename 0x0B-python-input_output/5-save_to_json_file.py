#!/usr/bin/python3
"""
Module works on files with JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """ Prints JSON rep of an object to file"""
    with open(filename, 'w') as open_file:
        open_file.write(json.dumps(my_obj))
