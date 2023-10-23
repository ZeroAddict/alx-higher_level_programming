#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0 # y is num of elements
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=" ")
            y = y + 1
        except IndexError:
            pass
    print("")
    return (y)
