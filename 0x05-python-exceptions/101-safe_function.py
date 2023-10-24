#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result_ptr = fct(*args)
    except BaseException as err:
        result_ptr = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return result_ptr
