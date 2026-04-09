def saveThePrisoner(n, m, s):
    remainder = (m - 1) % n
    if remainder + s > n:
        return (remainder + s) % n
    else:
        return remainder + s
