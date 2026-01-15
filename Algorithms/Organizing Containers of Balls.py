# If swapping can make all balls of one type into one container,
# the sum of row should equal the sum of column in this 2D array
# And there should be at least one valid block in each row and col

def organizingContainers(container):
    n = len(container)
    row_sum = [0] * n
    col_sum = [0] * n
    
    for i in range(n):
        for j in range(n):
            row_sum[i] += container[i][j]
            col_sum[j] += container[i][j]
            
    valid_rows = [False] * n
    valid_cols = [False] * n
    for i in range(n):
        for j in range(n):
            if row_sum[i] == col_sum[j]:
                valid_rows[i] = True
                valid_cols[j] = True
    
    for i in range(n):
        if valid_rows[i] is False:
            return "Impossible"
        if valid_cols[i] is False:
            return "Impossible"
    return "Possible"
