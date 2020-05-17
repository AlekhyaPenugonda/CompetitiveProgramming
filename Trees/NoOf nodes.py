class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count(root):
    if not root:
        return 0
    return 1 + count(root.left) + count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(count(root))