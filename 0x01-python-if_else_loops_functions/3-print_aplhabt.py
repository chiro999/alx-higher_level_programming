#!/usr/bin/python3
for _char in range(97, 123):
    if _char != 101 and _char != 113:
        print("{:c}".format(_char), end='')
