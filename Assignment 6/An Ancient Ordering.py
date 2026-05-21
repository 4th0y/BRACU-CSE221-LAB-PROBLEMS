import sys
from heapq import heappush, heappop
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n = int(input())
    words = [input().strip() for _ in range(n)]

    adj = defaultdict(set)
    indegree = {c: 0 for w in words for c in w}

    valid = True
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        found = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                found = True
                break
        
        if not found and len(w1) > len(w2):
            valid = False

    if not valid:
        print(-1)
        return

    heap = []
    for c in indegree:
        if indegree[c] == 0:
            heappush(heap, c)

    order = []
    while heap:
        c = heappop(heap)
        order.append(c)
        for nb in adj[c]:
            indegree[nb] -= 1
            if indegree[nb] == 0:
                heappush(heap, nb)

    if len(order) != len(indegree):
        print(-1)
        return

    print(''.join(order))

solve()