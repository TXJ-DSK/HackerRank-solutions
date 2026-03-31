from collections import deque
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    dq = deque([root])
    while dq:
        node = dq.popleft()
        print(node.info, end=" ")
        if node.left:
            dq.append(node.left)
        if node.right:
            dq.append(node.right)
