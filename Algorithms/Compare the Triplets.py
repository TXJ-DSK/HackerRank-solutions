def compareTriplets(a, b):
    A_score, B_score = 0, 0
    for i in range(3):
        if a[i] > b[i]:
            A_score += 1
        elif a[i] < b[i]:
            B_score += 1
    return [A_score, B_score]
