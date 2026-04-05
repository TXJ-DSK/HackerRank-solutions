def angryProfessor(k, a):
    count = 0
    for t in a:
        if t <= 0:
            count += 1
    return "YES" if count < k else "NO"
