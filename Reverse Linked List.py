"""
This problem comes from The Daily Coding Problem.

Given the head of a singly linked list, reverse it in-place.
Because the reversal is in place, the algorithm should run in O(n) time and
O(1) space.
"""

# Reverse Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sol(root):

    # Check for 1 or less node
    if root == None or root.next == None:
        return

    # Initialize pointers
    ptr_1 = root
    ptr_2 = ptr_1.next
    ptr_3 = ptr_2.next

    # Remove connection from the future tail
    ptr_1.next = None

    # Traverse and manipulate node pointers
    while ptr_3 != None:
        ptr_2.next = ptr_1
        ptr_1 = ptr_2
        ptr_2 = ptr_3
        ptr_3 = ptr_3.next

    # Manipulate node pointers at the head of Linked List
    ptr_2.next = ptr_1
    root = ptr_2

    # Return new root
    return root

# Test Code

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

root = node1
node1.next = node2
node2.next = node3
