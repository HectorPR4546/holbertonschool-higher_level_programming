#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list safely.

    Args:
        my_list (list): The list to print elements from.
        x (int): Number of elements to attempt to print.

    Returns:
        int: The number of elements actually printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
