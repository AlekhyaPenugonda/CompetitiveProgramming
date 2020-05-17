"""
Relationship between array indexes and tree element
A complete binary tree has an interesting property that we can use to find the children and parents of any node.

If the index of any element in the array is i, the element in the index 2i+1 will become the left child and element in 2i+2 index will become the right child. Also, the parent of any element at index i is given by the lower bound of (i-1)/2."""
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))


def isComplete(root, index, numberNodes):

    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (isComplete(root.left, 2 * index + 1, numberNodes)
            and isComplete(root.right, 2 * index + 2, numberNodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
