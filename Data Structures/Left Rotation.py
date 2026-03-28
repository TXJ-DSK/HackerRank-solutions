def rotateLeft(d, arr):
    d = d % len(arr)
    return arr[d:] + arr[:d]
