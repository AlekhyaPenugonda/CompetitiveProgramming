"""Perfect Binary Tree Theorems
A perfect binary tree of height h has 2**(h + 1) – 1 node.
A perfect binary tree with n nodes has height log(n + 1) – 1 = Θ(ln(n)).
A perfect binary tree of height h has 2**h leaf nodes.
The average depth of a node in a perfect binary tree is Θ(ln(n)).
"""



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    d = 0
    if not root:
        return d
    while(root):
        d += 1
        root = root.left
    return d
    

def is_perfect_binary_tree(root, d, level = 0):
    if not root:
        return True
    if root.left is None and root.right is None:
        return d == level+1
    if root.left is None or root.right is None:
        return False
    return is_perfect_binary_tree(root.left, d, level + 1) and is_perfect_binary_tree(root.right, d, level + 1)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
in_order(root)
d = depth(root)
print(is_perfect_binary_tree(root, d))