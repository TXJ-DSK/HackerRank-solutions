from collections import Counter
def pickingNumbers(a):
    cnt = Counter(a)
    result = 0
    for key in cnt:
        result = max(result, cnt[key]+cnt[key+1])
    return result
