from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, m, s, q = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[v].append(u)
        adj[u].append(v)

    sources = list(map(int, input().split()))
    destination = list(map(int, input().split()))

    dist = [-1] * (n + 1)
    q_bfs = deque()
    for src in sources:
        dist[src] = 0
        q_bfs.append(src)
        
    while q_bfs:
        u = q_bfs.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q_bfs.append(v)
    print(*[dist[d] for d in destination])

solve()
