def pageCount(n, p):
    front = p // 2
    lastpage = n
    if lastpage % 2 == 0:
        lastpage += 1
    end = (lastpage - p) // 2
    return min(front, end)
