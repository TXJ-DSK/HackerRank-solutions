def biggerIsGreater(w):
    if len(w) < 2:
        return "no answer"
    char_counter = Counter(w[-1])
    for i in range(len(w)-2, -1, -1):
        if w[i] >= max(char_counter.keys()):
            char_counter[w[i]] += 1
        else:
            prev = w[:i]
            char_counter[w[i]] += 1
            next_bigger = min([c for c in char_counter.keys() if c > w[i]])
            prev += next_bigger
            char_counter[next_bigger] -= 1
            keys = sorted(list(char_counter.keys()))
            for c in keys:
                prev += c * char_counter[c]
            return prev
    return "no answer"
