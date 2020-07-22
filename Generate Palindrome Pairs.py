"""
This problem comes from Daily Coding Problem:

Given a list of words, find all pairs of unique indices such that the
concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1,0), (2,3)].
"""

# Generate Palindrome Pairs

def isPalindrome(word):
    return word == word[::-1]

def sol(arr):
    solution = []
    for word in arr:
        for i in range(len(word)):
            if isPalindrome(word + word[i::-1]):
                if word[i::-1] in arr:
                    left,right = arr.index(word),arr.index(word[i::-1])
                    if [left,right] not in solution and left != right:
                        solution.append([left,right])
            if isPalindrome(word[i::-1] + word):
                if word[i::-1] in arr:
                    left,right = arr.index(word[i::-1]),arr.index(word)
                    if [left,right] not in solution and left != right:
                        solution.append([left,right])
    return solution
