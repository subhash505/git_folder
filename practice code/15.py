"""
2. Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
"""
import pandas as pd
import numpy as np

def main():
    input_list=[int (x) for x in input().split()]
    count_length=8
    len1=len(input_list)
    x=input_list[4]
    count1=0
    count1 =sum(map(lambda y: y==x,input_list))
    if count1==3 and len1== 8:
        print("TRUE")
    else:
        print("FALSE")

if __name__ =="__main__":
    main()
