#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely prints an integer using "{:d}".format.

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
