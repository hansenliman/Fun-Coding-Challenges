"""
This is not a coding challenge. This is my take on the Quick Sort algorithm.

It uses recursion and it's very easy for people trying to understand
why the algorithm is O(nlog(n)) run time!
"""

# Quick Sort
def quickSort(arr):
    print(arr)
    if len(arr) <= 1: # returns if it only has one element
        return arr
    pivot = arr.pop() # picks the last element as pivot
    left_arr = [] # create left and right arrays
    right_arr = []
    for i in arr: # sort the original array with the pivot
        if i <= pivot:
            left_arr.append(i)
        elif i > pivot:
            right_arr.append(i)
    left_arr = quickSort(left_arr) # recursively call quicksort
    right_arr = quickSort(right_arr)
    left_arr.append(pivot) # combine left_array + pivot + right_array
    return left_arr + right_arr
