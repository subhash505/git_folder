import numpy as np
import pandas as pd

# Exercise 1: Create a string made of the first, middle and last character
def main():
    str1= "subhash"
    length_string=len(str1)
    print(length_string)
    print(length_string//2)
    if ((length_string-1) %2)!=0:
        mid=(length_string-1)//2 +1
    else:
        mid= (length_string-1)//2
    print(str1[0]+str1[mid]+str1[length_string-1])


if __name__ == "__main__":
    main()