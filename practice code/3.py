import numpy as np
import pandas as pd

# Exercise3: Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
def main():
    s1=input()
    s2=input()
    s3=s1+s2+s1
    print(s3)

if __name__ == "__main__":
    main()
    