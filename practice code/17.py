<<<<<<< HEAD
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
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

"""
import pandas as pd
import numpy as np
# from memory_profiler import profile

# @profile
def main():
    input_1=int(input())
    len1=input_1
    last_term=input_1+(len1-1)*2
    #[(lambda x: x*x)(x) for x in range(10)]
    list1=[x for x in range(input_1,last_term+1,2)]
    # list2=list(map(lambda x : x+2 , range(input_1-2,last_term+1) ))
    #input_1 = int(input())
    # len1 = input_1
    # last_term = input_1 + (len1 - 1) * 2

    # list2 = list(filter(lambda x: (x % 2 == 0), range(input_1, last_term + 1)))
    print(list1)

    #print(list2)

    # input_1 = int(input())
    # len1 = input_1
    # last_term = input_1 + (len1 - 1) * 2
    # list2 = list(filter(lambda x: (x % 2 == 0), range(input_1, last_term + 1)))
    # print(list2)


if __name__ == "__main__":
=======
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
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

"""
import pandas as pd
import numpy as np

def main():
    input_1=int(input())
    len1=input_1
    last_term=input_1+(len1-1)*2
    #[(lambda x: x*x)(x) for x in range(10)]
    list1=[x for x in range(input_1,last_term+1,2)]
    print(list1)

if __name__ == "__main__":
>>>>>>> cdaff22cae5c65f7f7adf504612ab11f23ad3a15
    main()