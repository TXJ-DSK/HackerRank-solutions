def countingValleys(steps, path):
    count = 0
    altitude = 0
    isBelow = False
    for c in path:
        if c == 'U':
            altitude += 1
        elif c == 'D':
            altitude -= 1
        else:
            continue
        if altitude == 0:
            if isBelow:
                count += 1
                isBelow = False
        elif altitude < 0:
            isBelow = True
    return count
