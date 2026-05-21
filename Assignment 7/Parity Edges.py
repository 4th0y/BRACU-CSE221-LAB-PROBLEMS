import heapq
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))

    adj = [[]for _ in range(n + 1)]

    for i in range(m):
        u, v, w = u_list[i], v_list[i], w_list[i]
        adj[u].append((v, w))

    INF = float('inf')
    dist = [[INF] * 2 for _ in range(n + 1)]

    heap = [(0, 1, -1)]

    while heap:
        d, u, last_par = heapq.heappop(heap)
        if last_par != -1 and d > dist[u][last_par]:
            continue
        for v, w in adj[u]:
            curr_par = w % 2

            if curr_par == last_par:
                continue
            new_dist = d + w
            if new_dist < dist[v][curr_par]:
                dist[v][curr_par] = new_dist
                heapq.heappush(heap, (new_dist, v, curr_par))
    ans = min(dist[n][0], dist[n][1])
    print(ans if ans != INF else -1)
solve()