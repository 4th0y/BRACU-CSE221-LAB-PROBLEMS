import heapq
import sys
inpout = sys.stdin.readline

def solve():
    n, m, S, D = map(int, input().split())

    node_weight = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)

    dist = [float('inf')] * (n + 1)
    dist[S] = node_weight[S]

    heap = [(node_weight[S], S)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue
        for  v in adj[u]:
            new_cost = dist[u] + node_weight[v]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (dist[v], v))

    if dist[D] == float('inf'):
        print(-1)
    else:
        print(dist[D])

solve()