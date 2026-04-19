def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    curr = 0
    while True:
        energy -= 1
        curr = (curr + k) % n
        if c[curr] == 1:
            energy -= 2
        if curr == 0:
            break
    return energy
