def nonDivisibleSubset(k, s):
    if k == 1:
        return 1
    if len(s) == 1:
        return 1
    remainderCount = [0] * k
    result = 0
    for num in s:
        remainder = num % k
        remainderCount[remainder] += 1
    r_min = 1
    r_max = (k+1) // 2
    # find each remainder pair that can add to k
    # keep the bigger one in each pair
    for i in range(r_min, r_max):
        result += max(remainderCount[i],remainderCount[k-i])
    # if any number can be divided by k, can add one
    if remainderCount[0] >= 1:
        result += 1
    # if remainder is exactly k/2, can add one
    if k % 2 == 0 and remainderCount[k//2] >= 1:
        result += 1
    return result
