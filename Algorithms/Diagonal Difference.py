def diagonalDifference(arr):
    sum1, sum2 = 0, 0
    n = len(arr)
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n-1-i]
    return abs(sum1-sum2)
