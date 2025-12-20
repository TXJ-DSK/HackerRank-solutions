def matchingStrings(stringList, queries):
    query_dict = dict()
    results = [0] * len(queries)
    for idx, query in enumerate(queries):
        query_dict[query] = query_dict.get(query, [])
        # handles repeated string in queries
        query_dict[query].append(idx)
    for s in stringList:
        if s in query_dict:
            for idx in query_dict[s]:
                results[idx] += 1
    return results
