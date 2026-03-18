def hourglassSum(arr):
    result = -9 * 7
    for row in range(4):
        for col in range(4):
            hourglass = arr[row + 1][col + 1]
            for i in range(3):
                hourglass += arr[row][col + i]
                hourglass += arr[row+2][col + i]
            if hourglass > result:
                result = hourglass
    return result
