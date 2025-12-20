def extraLongFactorials(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    print(result)
