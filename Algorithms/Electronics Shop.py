def getMoneySpent(keyboards, drives, b):
    curr = -1
    keyboards.sort()
    drives.sort()
    d_idx = len(drives) - 1
    for k in keyboards:
        # loop through keyboard prices asec
        if k >= b:
            return curr
        while k + drives[d_idx] > b:
            d_idx -= 1
            if d_idx < 0:
                # reached minimum drive price, cannot find a pair
                return curr
        curr = max(curr, k + drives[d_idx])
    
    return curr
