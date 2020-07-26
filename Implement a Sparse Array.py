"""
Problem taken from Daily Coding Problems.

You have a large array, most of whose elements are zero.

Create a more space-efficient data structure, SparseArray, that implements the
following interface:

- init(arr, size): initialie with the original arge array and size.
- set(i, val): update index at i to be val.
- get(i): get the value at index i.
"""

# Implement a Sparse Array

class SparseArray:
    def __init__(self, arr, size): # Initialize with the original large array and size.
        self.dict = {}
        self.size = size
        for i in range(self.size - 1):
            if i != 0:
                self.dict[i] = arr[i]
                
    def set(self, i, val): # Update index at i to be val.
        self.dict[i] = val

    def get(self, i): # Get the value at index i.
        if i not in self.dict:
            return 0
        else:
            return self.dict[i]
