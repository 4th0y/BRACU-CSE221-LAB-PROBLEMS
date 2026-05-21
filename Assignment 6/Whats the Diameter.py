from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, n, adj):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest, max_dist = start, 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > max_dist:
                    max_dist = dist[v]
                    farthest = v
                q.append(v)
    
    return farthest, max_dist, dist

def solve():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    A, _, _ = bfs(1, n, adj)

    B, diameter, _ = bfs(A, n, adj)

    print(diameter)
    print(A, B)

solve()
