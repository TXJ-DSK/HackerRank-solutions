def height(root):
    if root is None:
        return 0
    if root.left is not None or root.right is not None:
        return max(height(root.left), height(root.right)) + 1
    else:
        return 0
