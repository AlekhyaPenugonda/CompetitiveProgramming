"""
Full Binary Tree Theorems
Let, i = the number of internal nodes
       n = be the total number of nodes
       l = number of leaves
      λ = number of levels
The number of leaves is i + 1.
The total number of nodes is 2i + 1.
The number of internal nodes is (n – 1) / 2.
The number of leaves is (n + 1) / 2.
The total number of nodes is 2l – 1.
The number of internal nodes is l – 1.
The number of leaves is at most 2λ - 1.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_full_binarytery(root):
    if not root:
        return True
    elif root.left == None and root.right == None:
        print(root.data)
        return True
    elif root.left != None and root.right != None:
        return is_full_binarytery(root.left) and  is_full_binarytery(root.right)
    return False

root = Node(1)
root.right = Node(3)
root.left = Node(2) 
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
print(is_full_binarytery(root))