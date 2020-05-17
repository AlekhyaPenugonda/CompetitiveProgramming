class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def ht(self, root):
        if not root:
            return 0
        return max(self.ht(root.left), self.ht(root.right)) + 1
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.ht(root.left) - self.ht(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
a = Solution()
print(a.isBalanced(root))
