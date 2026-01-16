def gcd(a: int, b: int) -> int:
    g = max(a, b)
    s = min(a, b)
    if s == 0:
        return g
    return gcd(g % s, s)

def lcm(a: int, b: int) -> int:
    g = max(a, b)
    s = min(a, b)
    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 

def getTotalX(a, b):
    lcm_a = 999
    gcd_b = 0
    if len(a) == 1:
        lcm_a = a[0]
    else:
        lcm_a = lcm(a[0], a[1])
        for i in range(2,len(a)):
            lcm_a = lcm(lcm_a, a[i])
    if len(b) == 1:
        gcd_b = b[0]
    else:
        gcd_b = gcd(b[0], b[1])
        for i in range(2,len(b)):
            gcd_b = gcd(gcd_b, b[i])
    count = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count
