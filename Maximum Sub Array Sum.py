"""
A classic maximum sub array problem, taken from Daily Coding Problem:

Given an array of numbers, find the maximum sum of any contigious subarray of the array.

Do this is O(n) time.

Example:

Given arr = [34, -50, 42, 14, -5, 86]
Return 137, since we would take elements 42, 14, -15, and 86.

Given arr = [-5, -1, -8, -9]
Return 0, since we would choose not to take any elements.
"""

# Maximum Sub Array Sum
def sol(arr):
    max_seen = curr = 0
    for i in arr:
        curr = max(curr + i, i)
        if curr > max_seen:
            max_seen = curr
    return max_seen
