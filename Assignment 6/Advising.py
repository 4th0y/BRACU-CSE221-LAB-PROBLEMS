import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        in_degree[b] += 1

    # ✅ Outside the for loop
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if len(order) != n:
        print(-1)
    else:
        print(*order)

t = int(input())  # ✅ input() not input
for _ in range(t):
    solve()