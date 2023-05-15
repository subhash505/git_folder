import numpy as np
import pandas as pd

"""
Exercise 4: Write a program to add item 7000 after 6000 in the following Python List
Given:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] """

def main():
    list1= [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    # for i in list1:
    #     if i < 7000:
    #         print(i)
    list1[2][2].append(7000)
    print(list1)

if __name__ == "__main__":
    main()

