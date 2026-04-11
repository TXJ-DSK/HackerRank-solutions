def permutationEquation(p):
    pos = dict()
    for i in range(len(p)):
        pos[p[i]] = i + 1
    firstOrder = []
    for i in range(len(p)):
        firstOrder.append(pos[i + 1])
    secondOrder = []
    for i in range(len(p)):
        secondOrder.append(pos[firstOrder[i]])
    return secondOrder
