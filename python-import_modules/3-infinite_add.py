#!/usr/bin/python3
"""
This script adds all command-line arguments passed to it and prints the result.

Usage:
    ./script_name.py 1 2 3
    Output: 6

Note:
    All arguments must be integers.
"""

import sys

if __name__ == "__main__":
    total_sum = 0
    for arg in sys.argv[1:]:
        total_sum += int(arg)
    print(total_sum)
