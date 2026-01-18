def breakingRecords(scores):
    highest, lowest = scores[0], scores[0]
    count_h, count_l = 0, 0
    for i in range(1, len(scores)):
        if scores[i] > highest:
            count_h += 1
            highest = scores[i]
        elif scores[i] < lowest:
            count_l += 1
            lowest = scores[i]
    return [count_h, count_l]
