from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, m, s, d = map(int, input().split())
    us = list(map(int, input().split()))
    vs = list(map(int, input().split()))


    graph = [[] for _ in range(n + 1)]
    for u, v in zip(us, vs):
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n + 1):
        graph[i].sort()

    
    if s == d:
        print(0)
        print(s)
        return
    
    dist = [-1] * (n + 1)
    dist[d] = 0
    queue = deque([d])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)


    if dist[s] == -1:
        print(-1)
        return

    path = [s]
    cur = s
    while cur != d:
        for v in graph[cur]:
            if dist[v] == dist[cur] - 1:
                path.append(v)
                cur = v
                break

    print(len(path) - 1)
    print(*path)

solve()