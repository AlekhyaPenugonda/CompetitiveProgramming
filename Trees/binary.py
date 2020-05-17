class binary_tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def insert_left(self, data):
        if self.left == None:
            self.left = binary_tree(data)
        else:
            t = binary_tree(data)
            t.left = self.left
            self.left = t

    def insert_right(self, data):
        if self.right == None:
            self.right = binary_tree(data)
        else:   
            t = binary_tree(data)
            t.right = self.right
            self.right = t

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end = " ")
        in_order(root.right)

n = binary_tree(5)
n.insert_left(3)
n.insert_right(7)
n.left.insert_left(2)
n.left.insert_right(4)
n.right.insert_left(6)
n.right.insert_right(8)
in_order(n)