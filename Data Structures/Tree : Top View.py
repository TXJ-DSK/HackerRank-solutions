from collections import deque
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    visible = dict()
    dq = deque()
    dq.append((root, 0))
    
    while dq:
        node, pos = dq.popleft()
        if pos not in visible:
            visible[pos] = node.info
        if node.left:
            dq.append((node.left, pos - 1))
        if node.right:
            dq.append((node.right, pos + 1))
    for pos in sorted(visible.keys()):
        print(visible[pos],end=" ")
