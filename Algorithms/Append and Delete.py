def appendAndDelete(s, t, k):
    repeated = 0
    for i in range(min(len(t),len(s))):
        if s[i] == t[i]:
            repeated += 1
        else:
            break
    needed = len(s) - repeated + (len(t) - repeated)
    print(needed)
    if needed > k:
        return "No"
    else:
        if (needed - k) % 2 == 0:
            return "Yes"
        elif k >= len(s) + len(t):
            return "Yes"
        else:
            return "No"
