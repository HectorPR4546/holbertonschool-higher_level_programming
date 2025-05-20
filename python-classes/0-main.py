#!/usr/bin/python3
Square = __import__('0-square').Square


my_square = Square()
print(type(my_square))        # Output: <class '0-square.Square'>
print(my_square.__dict__)     # Output: {}
