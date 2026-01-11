def timeConversion(s):
    ampm = s[-2:]
    if ampm == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    elif ampm == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            hr = s[:2]
            return str(int(hr)+12) + s[2:-2]
    else:
        return ""
