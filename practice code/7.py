import numpy as np
import pandas as pd

"""
Exercise 7: Write a program to unpack the following tuple into four variables and display each variable.
Given:
tuple1 = (10, 20, 30, 40)

"""
def main():
    dict1={}
    tuple1 = (10, 20, 30, 40)
    list1=['a','b','c','d']
    # for i in list1:
    #     dict1[i]=0
    dict1={ i:0 for i in list1}
    print(dict1)
    length=len(tuple1)
    # j=0
    # for i in dict1:
    #     dict1[i] = tuple1[j]
    #     print(tuple1[j])
    #     j+=1
    dict1 = {i: val for i, val in zip(dict1, tuple1)}
    print(*tuple1, sep='\n')

    print(dict1)   


if __name__ =="__main__":
    main()


