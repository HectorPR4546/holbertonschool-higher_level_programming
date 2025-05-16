#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list that are integers.
    Use "{:d}".format() to print each integer without a newline,
    then print a newline at the end.
    Return the number of integers printed.
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
