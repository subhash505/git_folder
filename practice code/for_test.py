
"""
4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
 If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible.
 Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
Output:

"""
import pandas as pd
import numpy as np
from memory_profiler import profile
from pympler import summary
import time

@profile
def main():
    inp_list=[int(x) for x in input().split(',')]
 
    start = time.time()
    count_19=0
    count_5=0
    count2=2
    count3=3
    for i in inp_list:
        if i == 19:
            count_19+=1
        if i == 5:
            count_5+=1
    if count_5==count3 and count_19==count2:
        print("TRUE")
    else:
        print("FALSE")
    
    end = time.time()
    print(end - start)
    
if __name__=="__main__":
    main()