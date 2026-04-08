def viralAdvertising(n):
    day = 1
    shared = 5
    cumulative = 0
    while day <= n:
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
        day += 1
    return cumulative
