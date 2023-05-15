import numpy as np
import pandas as pd

# Exercise 8: Swap two tuples in Python
# Given:
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# Expected output:
# tuple1: (99, 88)
# tuple2: (11, 22)

def main():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    tuple1, tuple2 = tuple2, tuple1
    # l1=list(tuple1)   #another method to that question
    # l2=list(tuple2)
    # print(l1)
    # print(l2)
    # for i in range(2):
    #     x=l1[i]
    #     l1[i]=l2[i]
    #     l2[i]=x
    # print(l1)
    # print(l2)
    # tuple1=tuple(l1)
    # tuple2=tuple(l2)
    print(tuple1)
    print(tuple2)

if __name__== "__main__":
    main()


