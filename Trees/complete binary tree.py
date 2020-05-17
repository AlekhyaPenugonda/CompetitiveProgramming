class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_perfect_binary_tree(root):
    if not root:
        return True
    if root.left is None and root.right is None or root.left is not None and root.right is None:
        return True
    if root.left is None and root.right is not None:
        return False
    return is_perfect_binary_tree(root.left) and is_perfect_binary_tree(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(is_perfect_binary_tree(root))