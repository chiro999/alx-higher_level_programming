#!/usr/bin/python3


def uppercase(str):
        for ltr in str:
        if ord(ltr) >= 97 and ord(ltr) <= 122:
            ltr = chr(ord(ltr) - 32)
        print("{}".format(ltr), end="")
    print("")
