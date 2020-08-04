"""
Problem taken from LeetCode

Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the 
different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        def recur(input):
            if input.isdigit():
                return [int(input)]
            new_arr = []
            for i in range(len(input)):
                if input[i] in "+-*":
                    eq_1 = recur(input[:i])
                    eq_2 = recur(input[i+1:])
                    for j in eq_1:
                        for k in eq_2:
                            new_arr.append(solve(j, k, input[i]))
            return new_arr
                
        def solve(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            else:
                return num1 * num2
            
        return recur(input)
