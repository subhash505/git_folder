import pandas as pd
import numpy as np

"""
Exercise 12: Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
Given:
list1 = [54, 44, 27, 79, 91, 41]
Expected Output:
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

"""
def main():
    list1 = [54, 44, 27, 79, 91, 41]

    sample_list = [34, 54, 67, 89, 11, 43, 94]

    print("Original list ", sample_list)
    element = sample_list.pop(4)
    print("List After removing element at index 4 ", sample_list)

    sample_list.insert(2, element)
    print("List after Adding element at index 2 ", sample_list)

    sample_list.append(element)
    print("List after Adding element at last ", sample_list)


if __name__=="__main__":
    main()