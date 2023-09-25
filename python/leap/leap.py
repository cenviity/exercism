"""This module contains a single function that tests if a given year is a leap year.
"""


def leap_year(year):
    """Determine whether a given year is a leap year.

    Args:
        year (int): A given year to be tested.

    Returns:
        bool: True if `year` is a leap year, otherwise False.
    """
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0
