"""
Binary Tree Inorder Traversal (Leet Code)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(root):
    return sol(root, [])

def sol(root, arr):
    if (root == None):
        return arr
    
    arr = sol(root.left, arr)
    arr.append(root.data)
    arr = sol(root.right, arr)

    return arr

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
