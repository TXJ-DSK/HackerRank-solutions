def miniMaxSum(arr):
    if len(arr) == 0:
        print("0 0")
        return
    min_num, max_num = arr[0], arr[0]
    arr_sum = 0
    for num in arr:
        arr_sum += num
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print(f"{arr_sum - max_num} {arr_sum - min_num}")
