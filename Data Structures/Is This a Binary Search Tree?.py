def check_binary_search_tree_(root):
    return recursive_check(root, sys.maxsize, -sys.maxsize-1)

def recursive_check(n, max_bound, min_bound):
    if n is None:
        return True
    if n.data >= max_bound or n.data <= min_bound:
        return False
    if n.left is None and n.right is None:
        return True
    if n.left is not None and n.left.data >= n.data:
        return False
    if n.right is not None and n.right.data <= n.data:
        return False
    return recursive_check(n.left, min(max_bound,n.data), min_bound) and recursive_check(n.right, max_bound, max(n.data, min_bound))
    
