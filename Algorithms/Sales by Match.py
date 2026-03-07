def sockMerchant(n, ar):
    cnt = Counter(ar)
    result = 0
    for k in cnt.keys():
        result += cnt[k]//2
    return result
