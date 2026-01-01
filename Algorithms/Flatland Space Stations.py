def flatlandSpaceStations(n, c):
    c.sort()
    max_dis = c[0] - 0
    max_dis = max(max_dis, n-1-c[-1])
    for i in range(len(c)-1):
        max_dis = max(max_dis, (c[i+1]-c[i])//2)
    return max_dis
