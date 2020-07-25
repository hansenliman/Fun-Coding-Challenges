"""
Problem taken from Daily Coding Problems.

Given a string of round, curly, and square opening and closing brackets, return whether
the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

# Determine Whether Brackets are Balanced

def sol(data):
    stack = []
    for char in data:
        if char in ['(', '{', '[']: # Check if opening bracket
            stack.append(char)
        else:
            if len(stack) == 0: # Check if there is no opening bracket
                return False
            if char == ')' and stack[-1] != '(': # Check if opening bracket match
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop() # If match, then pop opening bracket
    return len(stack) == 0 # Make sure that opening equals closing bracket
