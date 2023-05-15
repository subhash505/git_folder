import numpy as np
import pandas as pd

"""
Exercise 10: Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
Given:
tuple1 = (11, [22, 33], 44, 55)
Expected output:
tuple1: (11, [222, 33], 44, 55)

"""
def main():
    tuple1 = (11, [22, 33], 44, 55)
    l1=list(tuple1)
    print(tuple1)
    x=str(tuple1[1][0])
    print(x)
    x=x+"2"
    l1[1][0]=int(x)
    tuple1=tuple(l1)
    print(tuple1)

if __name__=="__main__":
    main()