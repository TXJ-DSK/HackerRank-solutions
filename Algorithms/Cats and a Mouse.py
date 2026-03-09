def catAndMouse(x, y, z):
    a_distance = abs(x - z)
    b_distance = abs(y - z)
    if a_distance == b_distance:
        return "Mouse C"
    elif a_distance < b_distance:
        return "Cat A"
    else:
        return "Cat B"
