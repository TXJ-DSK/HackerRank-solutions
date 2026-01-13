def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    for i in apples:
        if a+i >= s and a+i <= t:
            count_apple += 1
    count_orange = 0
    for i in oranges:
        if b+i >= s and b+i <= t:
            count_orange += 1
    print(count_apple)
    print(count_orange)
