def circularArrayRotation(a, k, queries):
    n = len(a)
    return [a[(i - k) % n] for i in queries]
