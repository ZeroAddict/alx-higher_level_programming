#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    div_by_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_by_two.append(True)
        else:
            div_by_two.append(False)

    return (div_by_two)
