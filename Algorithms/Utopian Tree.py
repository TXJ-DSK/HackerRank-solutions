def utopianTree(n):
    period = 0
    height = 1
    while period < n:
        if period % 2 == 0:
            height *= 2
        else:
            height += 1
        period += 1
    return height
