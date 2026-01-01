def timeInWords(h, m):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight"
    , "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if m == 0:
        return words[h-1] + " o' clock"
    elif m == 15:
        return "quarter past " + words[h-1]
    elif m == 30:
        return "half past " + words[h-1]
    elif m == 45:
        return "quarter to " + words[h]
    elif m == 1:
        return "one minute past " + words[h-1]
    elif m == 59:
        return "one minute to " + words[h]
    mid = ""
    if m < 30:
        mid = " minutes past "
    else:
        mid = " minutes to "
        m = 60 - m
        h += 1
    result = ""
    if m > 20:
        result = "twenty "
        m = m - 20
    result += words[m-1]
    result += mid
    result += words[h-1]
    return result
