import heapq
from collections import Counter
def median(a,x):
    lo = []  # max-heap
    hi = []  # min-heap (same size as or one smaller than lo)
    n = len(a)
    cnt = Counter()
    for i in range(n):
        op = a[i]
        val = x[i]
        if op == 'a':
            cnt[val] += 1
            med = 0
            if len(lo) == len(hi):
                heapq.heappush_max(lo, heapq.heappushpop(hi, val))
                med = lo[0]
            else:
                heapq.heappush(hi, heapq.heappushpop_max(lo, val))
                med = (lo[0] + hi[0]) / 2
            if int(med) == med:
                print(int(med))
            else:
                print(med)
        if op == 'r':
            #print(f"i={i}",cnt)
            #print(f"lo={lo},hi={hi}")
            if len(lo) == 0:
                print("Wrong!")
                continue
            if cnt[val] == 0:
                print("Wrong!")
                continue
            med = lo[0]
            if len(lo) == len(hi):
                med = (lo[0] + hi[0]) / 2
            #print(f"med={med}")
            if val <= med:
                lo.remove(val)
                heapq.heapify_max(lo)
            else:
                hi.remove(val)
                heapq.heapify(hi)
            cnt[val] -= 1
            if len(lo) < len(hi):
                heapq.heappush_max(lo, heapq.heappop(hi))
            if len(lo) == 0:
                print("Wrong!")
                continue
            med = lo[0]
            if len(lo) == len(hi):
                med = (lo[0] + hi[0]) / 2
            if int(med) == med:
                print(int(med))
            else:
                print(med)
