#!/usr/bin/python3

import sys

arg = " ".join(sys.argv[1:])

for char in arg:
    if char.upper() != char.lower():
        print("[{0}{1}]".format(char.upper(), char.lower()), end="")
    else:
        print(char, end="")

print()
