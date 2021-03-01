"""
Product of Array Except Self (Leet Code)

Given an array nums of n integers where n > 1, return an array
output such that output[i] is equal to the product of all the elements
of nums except nums[i].

Example:
Input: [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

"""

def productOfArray(arr):
    arr1 = []
    arr2 = []
    sol = []
    curr = 1
    for i in arr:
        curr = curr * i
        arr1.append(curr)
    arr.reverse()
    curr = 1
    for i in arr:
        curr = curr * i
        arr2.append(curr)
    arr2.reverse()
    
    for i in range(len(arr)):
        arr1_ptr = i - 1
        arr2_ptr = i + 1

        if (arr1_ptr < 0):
            left = 1
            right = arr2[arr2_ptr]
        elif (arr2_ptr > len(arr) - 1):
            right = 1
            left = arr1[arr1_ptr]
        else:
            left = arr1[arr1_ptr]
            right = arr2[arr2_ptr]

        sol.append(left * right)

    return sol        
