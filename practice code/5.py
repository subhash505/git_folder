import numpy as np
import pandas as pd


"""
Exercise 5: The given tuple is a nested tuple. write a Python program to print the value 20.
Given:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
"""
def main():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    print(tuple1[1][1])


if __name__== "__main__":
    main()
    