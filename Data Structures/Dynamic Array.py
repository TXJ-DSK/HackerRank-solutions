def dynamicArray(n, queries):
    arrs = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    for q in queries:
        #print(arrs)
        idx = (q[1] ^ lastAnswer) % n
        #print(f"q[1]={q[1]},lastAnswer={lastAnswer},idx={idx}")
        if q[0] == 1:
            arrs[idx].append(q[2])
        elif q[0] == 2:
            lastAnswer = arrs[idx][q[2] % len(arrs[idx])]
            result.append(lastAnswer)
        else:
            pass
    return result
