def arrayManipulation(n, queries):
    operations = dict()
    for q in queries:
        operations[q[0]] = operations.get(q[0], 0) + q[2]
        operations[q[1]+1] = operations.get(q[1]+1, 0) - q[2]
    sorted_keys = sorted(list(operations.keys()))
    max_val = 0
    curr_val = 0
    for key in sorted_keys:
        curr_val += operations[key]
        if curr_val > max_val:
            max_val = curr_val
    return max_val
