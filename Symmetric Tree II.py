"""
Symmetric Tree II

Given a binary tree, check whether it is a mirror of itself.

For example, this binary tree is symmetric: 

     1
   /   \
  2     2
 / \   / \
3   4 4   3

But the following is not:

    1
   / \
  2   2
   \   \
   3    3

     1
   /   \
  2     5
 / \   / \
3   1 4   7

"""

class Node():
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sol(root):
    if root == None:
        return True
    return bfs(root.left,root.right)

def bfs(left,right):
    
    if (left == None and right == None):
        return True

    if (left != None and right != None and left.data == right.data):
        return bfs(left.left, right.right) and bfs(left.right, right.left)

    return False

# Test Tree
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
