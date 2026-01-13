def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    if v1 == v2:
        return "NO"
    initial_gap = 0
    speed_diff = 0
    if x1 < x2:
        initial_gap = x2 - x1
        speed_diff = v1 - v2
    else:
        initial_gap = x1 - x2
        speed_diff = v2 - v1
    if speed_diff <= 0:
        return "NO"
    if initial_gap % speed_diff == 0:
        return "YES"
    else:
        return "NO"
