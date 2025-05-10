#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':  # Check if char is lowercase
            ascii_upper = ord(char) - 32  # Convert to uppercase
            print(chr(ascii_upper), end='')  # Print the uppercase character
        else:
            print(char, end='')  # Print the character as it is
    print()  # Print a new line at the end
