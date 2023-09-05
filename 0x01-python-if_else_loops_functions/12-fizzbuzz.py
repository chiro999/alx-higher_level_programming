#!/usr/bin/python3

def fizzbuzz():
    for _num in range(1, 101):
        if _num % 3 == 0 and _num % 5 == 0:
            print("FizzBuzz ", end="")
        elif _num % 3 == 0:
            print("Fizz ", end="")
        elif _num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(_num), end="")
