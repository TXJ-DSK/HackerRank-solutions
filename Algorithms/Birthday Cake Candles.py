def birthdayCakeCandles(candles):
    if len(candles) == 0:
        return 0
    max_num = candles[0]
    count = 0
    for num in candles:
        if num > max_num:
            count = 1
            max_num = num
        elif num == max_num:
            count += 1
    return count
