"""
Problem taken from LeetCode:

Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        two = three = five = 0
        for i in range(n-1):
            uglyNum = min(2 * arr[two], 3 * arr[three], 5 * arr[five])
            if uglyNum == 2 * arr[two]:
                two += 1
            if uglyNum == 3 * arr[three]:
                three += 1
            if uglyNum == 5 * arr[five]:
                five += 1
            arr.append(uglyNum)
        return arr[-1]
