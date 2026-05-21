import heapq
import sys
input = sys.stdin.readline

def djikstra(start, adj, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

def solve():
    n, m, S, T = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    dist_alice = djikstra(S, adj, n)
    dist_bob = djikstra(T, adj, n)

    ans_time = float('inf')
    ans_node = -1

    for node in range(1, n + 1):
        if dist_alice[node] == float('inf') or dist_bob[node] == float('inf'):
            continue
        meet_time = max(dist_alice[node], dist_bob[node])
        if meet_time < ans_time or (meet_time == ans_time and node < ans_node):
            ans_time = meet_time
            ans_node = node

    if ans_node == -1:
        print(-1)

    else:
        print(ans_time, ans_node)
solve()
