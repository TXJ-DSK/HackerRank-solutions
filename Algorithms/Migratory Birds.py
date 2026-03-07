def migratoryBirds(arr):
    cnt = Counter(arr)
    most_common = cnt.most_common(1)[0]
    min_id, max_occurrence = most_common[0], most_common[1]
    for k in cnt.keys():
        if k < min_id and cnt[k] == max_occurrence:
            min_id = k
    return min_id
