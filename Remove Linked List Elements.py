"""
Remove Linked List Elements (Leet Code)

Remove all elements from a linked list
of integers that have value val.

Example:

Input: 1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

class Node:
        def __init__(self, data):
                self.data = data
                self.next = None

def removeNodes(val, root):
        
        while (root != None and root.data == val): # make sure that root has a node and check if root is the value
                root = root.next

        if (root == None): # check if root is empty
                return root
        
        ptr_1 = root
        ptr_2 = root.next

        while (ptr_2 != None): # normal routine
                if (ptr_2.data == val):
                        ptr_1.next = ptr_2.next
                        ptr_2 = ptr_2.next
                else:
                        ptr_1 = ptr_1.next
                        ptr_2 = ptr_2.next
                
        return root

def printNodes(root):
        print("Root -> ", end="")
        while (root != None):
                print(str(root.data) + " -> ", end="")
                root = root.next
        print("None")
                        
root = Node(1)
root.next = Node(2)
root.next.next = Node(6)
root.next.next.next = Node(3)
root.next.next.next.next = Node(4)
root.next.next.next.next.next = Node(5)
root.next.next.next.next.next.next = Node(6)

