#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely prints an integer value.

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
