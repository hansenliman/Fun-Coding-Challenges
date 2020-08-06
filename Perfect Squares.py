"""
Problem taken from LeetCode:

Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

def numSquares(n):
    
    dict = {}
    dict[0] = 0
    dict[1] = 1
    
    for i in range(2, n+1):
        curr = 1
        min_sol = i
        while(curr * curr <= i):
            temp_num = i - curr * curr
            if(1 + dict[temp_num] < min_sol):
                min_sol = 1 + dict[temp_num]
            curr += 1
            temp_num = i
        dict[i] = min_sol
        
    return dict[n]
