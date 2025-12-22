def climbingLeaderboard(ranked, player):
    uniqueRanked = [ranked[0]]
    for i in ranked[1:]:
        if i != uniqueRanked[-1]:
            uniqueRanked.append(i)
    result = []
    pos = len(uniqueRanked)
    for i in range(len(player)):
        while pos > 0 and player[i] >= uniqueRanked[pos-1]:
            pos -= 1
        result.append(pos+1)
    return result
