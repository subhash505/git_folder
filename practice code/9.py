import numpy as np
import pandas as pd

"""
Exercise 9: Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
Given:
tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:
tuple2: (44, 55)

"""
def main():
    tuple1 = (11, 22, 33, 44, 55, 66)
    tuple2=tuple()
    tuple2 = tuple(filter(lambda x: x // 11 == 4 or x // 11 == 5, tuple1))
    # for i in tuple1:    another way of doing the code.
    #     if (i//11==4) or (i//11 ==5):
    #         tuple2+= (i,)
    #tuple2=(tuple(map(lambda x: ((x//11 == 4) or (x//11 == 5))), tuple1))
    print(tuple2)

if __name__ =="__main__":
    main()
