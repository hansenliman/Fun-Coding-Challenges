"""
Symmetric Tree

Given a binary tree, check whether it is structurally a mirror of itself.
For this problem, the value does not have to be the same.

For example, this binary tree is symmetric: 

     1
   /   \
  2     5
 / \   / \
3   1 4   7

But the following is not:

    1
   / \
  2   2
   \   \
   3    3

"""

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sol(root):

    if (root == None):
        return True

    q_left = [root.left]
    q_right = [root.right]

    while (len(q_left) != 0 and len(q_right) != 0):

        curr_left = q_left.pop(0)
        curr_right = q_right.pop(0)

        if (curr_left != None):
            q_left.append(curr_left.left)
            q_left.append(curr_left.right)

        if (curr_right != None):
            q_right.append(curr_right.right)
            q_right.append(curr_right.left)

        if (len(q_left) != len(q_right)):
            return False

    return True

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
