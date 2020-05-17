""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

"""def check_binary_search_tree_(root):
    if not root or root.left == root.right == None:
        return True
    elif (root.left.data < root.data and root.right.data > root.data):
        return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)
    return False"""
# Above all testcases not executed

def inOrder(root, stack=[]):
    if root.left:
        inOrder(root.left, stack)
    stack.append(root.data)
    if root.right:
        inOrder(root.right, stack)

        
def check_binary_search_tree_(root):
    stack = []
    inOrder(root, stack)
    length = len(stack)
    for i in range(length-1):
        if stack[i] >= stack[i+1]:
            return False
    return True

# Finding max in left and min in right trees

class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10

# using inorder traversal

tree_vals = []

class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None
        
def inorder(tree):
    if tree != None:
        inorder(tree.left)
        tree_vals.append(tree.value)
        inorder(tree.right)
        
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)


root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

inorder(root) # prints True, since this tree is valid
print(sort_check(tree_vals))

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

inorder(root) # prints True, since this tree is valid
print(sort_check(tree_vals))

# To calculate time

%timeit inorder(root)