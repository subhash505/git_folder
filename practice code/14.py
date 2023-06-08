"""
1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""
# importing the module
import tracemalloc
import pandas as pd
import numpy as np
import time



# print(23*2.3)


def main():
    inp_list=[int(x) for x in input().split(',')]
 
    start = time.time()
    count_19=0
    count_5=0
    count2=2
    count3=3
    # for i in inp_list:
    #     if i == 19:
    #         count_19+=1
    #     if i == 5:
    #         count_5+=1
    
    count_19 = sum(map(lambda x: x == 19, inp_list))
    count_5 = sum(map(lambda x: x == 5, inp_list))
    if count_5==count3 and count_19==count2:
        print("TRUE")
    else:
        print("FALSE")
    
    end = time.time()
    print(end - start)
    
if __name__=="__main__":
    main()

"""


 
# code or function for which memory
# has to be monitored
def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)
 
# starting the monitoring
tracemalloc.start()
 
# function call
app()
 
# displaying the memory
print(tracemalloc.get_traced_memory())
 
# stopping the library
tracemalloc.stop()"""