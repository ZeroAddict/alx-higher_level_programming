#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for a, b in a_dictionary.items():
        if b > maxval:
            maxval = b
            maxkey = a
    return maxkey
