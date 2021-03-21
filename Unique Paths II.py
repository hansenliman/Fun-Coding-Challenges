"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""

def uniquePaths(arr):
    dp = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]

    for i in range(1,len(arr)): # fill up first row
        if arr[i][0] == 1:
            dp[i][0] = -1
        else:
            if dp[i-1][0] != -1:
                dp[i][0] = 1

    for j in range(1,len(arr[0])): # fill up first column
        if arr[0][j] == 1:
            dp[0][j] = -1
        else:
            if dp[0][j-1] != -1:
                dp[0][j] = 1

    for i in range(1,len(arr)):
        for j in range(1,len(arr[i])):
            if arr[i][j] == 1:
                dp[i][j] = -1
            else:
                up = 0
                left = 0
                if dp[i-1][j] != -1:
                    up = dp[i-1][j]
                if dp[i][j-1] != -1:
                    left = dp[i][j-1]
                dp[i][j] = up + left

    return dp[len(dp) - 1][len(dp[0]) - 1]
