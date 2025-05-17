#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers in a list.
    
    Args:
        my_list: List containing elements of any type
        x: Number of elements to access in my_list
        
    Returns:
        The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
    print()
    return count
