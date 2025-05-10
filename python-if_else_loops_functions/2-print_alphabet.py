#!/usr/bin/python3
i = 'a'
while ord(i) <= ord('z'):
    print ((i), end=""),
    i = chr(ord(i) + 1)
