"""
3. Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""
import numpy as np
import pandas as pd

def main():
    input_1=int(input())
    greater=pow(4,4)
    if input_1 > pow(4,4) and (input_1 % 34)==4:
        print("TRUE")
    else:
        print("FALSE")
if __name__ =="__main__":
    main()
    