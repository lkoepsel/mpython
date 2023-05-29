# Prints known error codes
import os
import errno


mpython_keys = [1, 2, 5, 9, 11, 12, 13, 17, 19, 21, 22, 95, 98, 103, 104,
                105, 107, 110, 111, 113, 114, 115]


for key in errno.errorcode.keys():
    if key in mpython_keys:
        print(f"{key} {errno.errorcode[key]} {os.strerror(key)} ")
