class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.recInsert(self.root, val)
    def recInsert(self, node, val):
        if val < node.info:
            if node.left is None:
                node.left = Node(val)
            else:
                self.recInsert(node.left, val)
        elif val > node.info:
            if node.right is None:
                node.right = Node(val)
            else:
                self.recInsert(node.right, val)
