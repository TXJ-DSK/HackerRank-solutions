def lca(root, v1, v2):
    if root.info == v1 or root.info == v2:
        return root
    elif v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    elif v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)
    else:
        return root
