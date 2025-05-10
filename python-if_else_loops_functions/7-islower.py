#!/usr/bin/python3
def islower(c):
    # Get the ASCII value of the character
    ascii_value = ord(c)
    # Check if it's in the range of lowercase letters
    return 97 <= ascii_value <= 122  # Returns True if c is lowercase
