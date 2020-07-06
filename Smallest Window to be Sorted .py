"""
Problem taken from Daily Coding Problem:

Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted.

Example:

Given nums = [3, 7, 5, 6, 9]

Because between nums[0] and nums[3] is where the array is unsorted,
return [1,3]
"""

#Smallest Window to be Sorted 
def sol(arr):
    left, right = None, None
    min_seen, max_seen = float("inf"), -float("inf")
    for i in range(len(arr)):
        max_seen = max(max_seen, arr[i])
        if arr[i] < max_seen:
            right = i
    for i in range(len(arr) - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i
    return left, right
