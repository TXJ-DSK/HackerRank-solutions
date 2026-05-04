def squares(a, b):
    lower = math.ceil(math.sqrt(a))
    upper = math.floor(math.sqrt(b))
    return upper-lower+1
