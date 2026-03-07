def dayOfProgrammer(year):
    leap = False
    if year == 1918:
        return '25.09.1918'
    if year < 1918 and year % 4 == 0:
        leap = True
    if year > 1918 and year % 4 == 0 and year % 100 != 0:
        leap = True
    if leap:
        return '12.09.'+str(year)
    else:
        return '13.09.'+str(year)
