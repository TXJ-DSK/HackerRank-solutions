from collections import deque

def swapNodes(indexes, queries):
    results = []
    depths = dict() # mapping 1-based index to node depth
    depths[1] = 1
    for i in range(len(indexes)):
        arr = indexes[i]
        idx = i + 1 # actual 1-based index
        if arr[0] != -1:
            depths[arr[0]] = depths[idx] + 1
        if arr[1] != -1:
            depths[arr[1]] = depths[idx] + 1
    for q in queries:
        for i in range(len(indexes)):
            idx = i+1
            if depths[idx] % q == 0:
                swap(indexes, idx)
        results.append(inorder(indexes))
    return results

def swap(indexes, idx):
    temp = indexes[idx - 1][0]
    indexes[idx - 1][0] = indexes[idx - 1][1]
    indexes[idx - 1][1] = temp
   
def inorder(indexes):
    result = []
    stack = deque([1])
    visited = set()
    while stack:
        idx = stack.pop()
        if idx >= len(indexes):
            visited.add(idx)
        if idx in visited:
            result.append(idx)
        else:
            visited.add(idx)
            arr = indexes[idx - 1]
            # FILO, push to stack in order right, root, left
            if arr[1] != -1:
                stack.append(arr[1])
            stack.append(idx)
            if arr[0] != -1:
                stack.append(arr[0])
    return result
