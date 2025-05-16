#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first x integers in a list.

    Args:
        my_list (list): The list containing elements.
        x (int): The number of elements to attempt to print.

    Returns:
        int: The number of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return count
