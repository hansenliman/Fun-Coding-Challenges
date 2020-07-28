"""
Problem taken from Daily Coding Problems.

A unival tree (which stands for "universal value") is a tree where
all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""

# Count Unival Trees

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sol(root):
    if root == None:
        return 0
    total, valid = countUnival(root)
    return total

def countUnival(root):
    if root.right == None and root.left == None: # Test for leaf node
        return 1, True
    total, valid = 0, False
    
    if root.left != None: # Case if left node is empty
        left_total, left_valid = countUnival(root.left)
    else:
        left_total, left_valid = 0, True
    if root.right != None: # Case if right node is empty
        right_total, right_valid = countUnival(root.right)
    else:
        right_total, right_valid = 0, True
    total = left_total + right_total # Sum total of left and right subtree 
    
    if left_valid and right_valid: # Check if tree is unival
        if root.left.data == root.right.data and root.left.data == root.data:
            return total + 1, True
    return total, False

# Test Code

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
