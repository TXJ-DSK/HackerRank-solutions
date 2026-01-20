def birthday(s, d, m):
    if len(s) < m:
        return 0
    count = 0
    int_sum = 0
    for i in range(m):
        int_sum += s[i]
    if int_sum == d:
        count += 1
    for i in range(m, len(s)):
        int_sum -= s[i - m]
        int_sum += s[i]
        if int_sum == d:
            count += 1
    return count
