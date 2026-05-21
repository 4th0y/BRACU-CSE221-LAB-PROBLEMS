import heapq
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    heap= [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            new_danger = max(dist[u], w)
            if new_danger < dist[v]:
                dist[v] = new_danger
                heapq.heappush(heap, (dist[v], v))

    result = []
    for i in range(1, n + 1):
        if dist[i] == float('inf'):
            result.append(-1)
        else:
            result.append(dist[i])
    print(*result)

solve()