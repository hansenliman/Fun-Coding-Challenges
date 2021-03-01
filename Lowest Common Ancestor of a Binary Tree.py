"""
Lowest Common Ancestor of a Binary Tree (Leet Code)

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in a tree.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).

Given the following binary:
root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: p = 5, q = 1
Output: 3

Explanation:
The LCA of the nodes 5 and 1 is 3.

Example 2:
Input: p = 5, q = 4
Output: 5

Explanation:
The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the definition.

Note:
- All of the nodes' values will be unique.
- p and q are different and both values will exist in the tree.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(root, p, q):
    foundAncestor, value = sol(root, p, q, False)
    if (not foundAncestor):
        return 0
    else:
        return value

def sol(root, p, q, foundDescendant): # Returns: descendantFound, ancestoryVal
    isDescendant = False
    if (root == None): # If leaf node
        return False, None
    if (root.data == p or root.data == q): # If current node is val
        if (foundDescendant): # If descendant is already found
            return True, None
        else: # Descendant might still be ancenstor
            isDescendant = True
            foundDescendant = True
    left_foundDescendant, left_val = sol(root.left, p, q, foundDescendant)
    right_foundDescendant, right_val = sol(root.right, p, q, foundDescendant)

    if (not left_foundDescendant and not right_foundDescendant and isDescendant): # If left and right returns false, but current node is a descendant
        return True, root.data
    if (left_foundDescendant and right_foundDescendant): # If descendant found in left or right
        return True, root.data
    if ((left_foundDescendant or right_foundDescendant) and foundDescendant and not isDescendant): # If current node receives a True but is not the other descendant
        return True, None
    if ((left_foundDescendant or right_foundDescendant) and foundDescendant and isDescendant): # If current node receives a True and is the other descendant
        return True, root.data
    if ((left_foundDescendant or right_foundDescendant) and not foundDescendant and not isDescendant): # If the node didn't find descendant, isn't a descendant but left/right returns True.
        if (left_foundDescendant):
            return True, left_val
        else:
            return True, right_val
    else:
        return False, None

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
