"""
Problem from LeetCode:

House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        def sol(arr):
            dp = []
            dp.append(arr[0])
            dp.append(max(arr[0],arr[1]))
            for i in range(2, len(arr)):
                dp.append(max(dp[i-2] + arr[i], dp[i-1]))
            return dp[-1]
        
        arr_1 = nums.copy()
        arr_2 = nums.copy()
        arr_1.pop(0)
        arr_2.pop()
        return max(sol(arr_1), sol(arr_2))
