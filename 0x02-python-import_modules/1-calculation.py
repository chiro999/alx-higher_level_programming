#!/usr/bin/python3

if __name__ == "__main__":
    """Print the 10+5, 10-5, 10*5 and 10/5"""
    from calculator_1 import sub, mul, div, add

    a = 10
    b = 5

    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} + {} = {}".format(a, b, add(a, b)))
