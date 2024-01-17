"""
1. Write a short programme that, when given a date, calculates the age between the current date and the given date.
  1. An example input and output might look like:
    1. 01-01-1990 should return 31
    2. 04-12-1972 should return 48
"""

# import modules
from datetime import date
from math import floor


def get_age(year, month, day):
    """
    Function to calculate the age of a person given a date
    """
    # convert to a date object
    given_date = date(year, month, day)

    # get the current date
    current_date = date.today()

    # subtract current date and given date to get the difference, divide by 365 and round down to get age in years
    difference = (current_date - given_date).days
    age = floor((difference / 365))
    return age


print(get_age(2010, 1, 1))
print(get_age(1972, 12, 4))
