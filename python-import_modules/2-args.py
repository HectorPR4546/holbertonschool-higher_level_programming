#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Get the list of arguments (excluding the script name)

    num_args = len(args)  # Get the number of arguments

    # Print the number of arguments
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:", end="")

    # Print a dot if no arguments were passed
    if num_args == 0:
        print(".")
    else:
        print()  # Print a new line

        # Print each argument
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")  # Print the position and value of each argument
