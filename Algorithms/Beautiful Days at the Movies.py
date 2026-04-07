def beautifulDays(i, j, k):
    count = 0
    for num in range(i, j+1):
        if abs(num - reverseInt(num)) % k == 0:
            count += 1
    return count

def reverseInt(i):
    s = str(i)
    s = s[::-1]
    return int(s)
