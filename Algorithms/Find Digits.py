def findDigits(n):
    int_divisors = [0]
    for i in range(1,10):
        if n % i == 0:
            int_divisors.append(1)
        else:
            int_divisors.append(0)
    count = 0
    while n > 0:
        number = n % 10
        count += int_divisors[number]
        n = n // 10
    return count
