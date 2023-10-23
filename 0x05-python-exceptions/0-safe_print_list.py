#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = x # y is num of elements

    for num in range(x):
        try:
            print("{}".format(my_list[num]), end=" ")
            y += 1
    
        except IndexError:
            break

    print("")
    return x
