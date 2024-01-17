"""
Given a list of integers, return the highest and lowest numbers in the array (without using max() or min())
Some example inputs and outputs would look like the below:
    1. [2, 4, 1, 0, 2, -1] should return the array [-1, 4] 
    2. [20, 50, 12, 6, 14, 8] should return the array [6, 50] 
    3. [100, -100] should return the array [-100, 100] 
"""

from math import inf


def get_lowest_and_highest(list_of_integers):
    """Given a list of integers, returns the highest and lowest numbers in the array"""
    # create empty list
    lowest_and_highest = []

    # get min
    min = +inf
    for num in list_of_integers:
        if num < min:
            min = num
    lowest_and_highest.append(min)

    # get max
    max = -inf
    for num in list_of_integers:
        if num > max:
            max = num
    lowest_and_highest.append(max)

    return lowest_and_highest


print(get_lowest_and_highest([2, 4, 1, 0, 2, -1]))
print(get_lowest_and_highest([20, 50, 12, 6, 14, 8]))
print(get_lowest_and_highest([100, -100]))
