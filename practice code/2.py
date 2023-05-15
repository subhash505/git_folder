import numpy as np
import pandas as pd

# Exercise 2: Write a program to create a new string made of the middle three characters of an input string.
def main():
    a=input()
    mid=len(a)//2
    x=a[mid-1:mid+2]
    print(x)


if __name__=="__main__":
    main()
