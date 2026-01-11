def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            remainder = grade % 5
            if remainder > 2:
                result.append(grade + 5 - remainder)
            else:
                result.append(grade)
    return result
