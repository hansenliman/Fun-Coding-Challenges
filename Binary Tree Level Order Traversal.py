"""
Binary Tree Level Order Traversal (Leet Code)

Given the root of a binary tree, return the level order traversal
of its nodes' values. (i.e., from left to right, level by level).

Example:
Input: root= = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if (root == None):
        return []
    
    queue = [root]

    level = 0
    sol = []
    while (len(queue) != 0):
        sub_sol = []
        temp = []
        for node in queue:
            sub_sol.append(node.data)
            if (node.left):
                temp.append(node.left)
            if (node.right):
                temp.append(node.right)
        sol.append(sub_sol)
        queue = temp
    return sol
            
# Test Tree
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
