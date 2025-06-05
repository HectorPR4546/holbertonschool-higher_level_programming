#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout."""
    # Open the file in read mode with UTF-8 encoding
    with open(filename, mode="r", encoding="utf-8") as file:
        # Print the file content without adding extra newline
        print(file.read(), end="")
