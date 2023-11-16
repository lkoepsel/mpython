#!/usr/local/bin/python3
# Prints known error codes for MicroPython
# Run in CPython (desktop Python) to obtain long error codes
import os
import errno


mpython_keys = [1, 2, 5, 9, 11, 12, 13, 17, 19, 21, 22, 95, 98, 103, 104,
                105, 107, 110, 111, 113, 114, 115]


print(f"Known MicroPython Error Codes with text")
for key in sorted(errno.errorcode.keys()):
    if key in mpython_keys:
        print(f"{key} {errno.errorcode[key]} {os.strerror(key)} ")
