import heapq
import sys
input = sys.stdin.readline

def solve():
    n, m, s, D = map(int, input().split()) 

    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))  

    adj = [[] for _ in range(n + 1)] 
    for i in range(m):
        u, v, w = u_list[i], v_list[i], w_list[i]
        adj[u].append((v, w))

    dist = [float('inf')] * (n + 1)
    dist[s] = 0

    prev = [-1] * (n + 1)

    heap = [(0, s)]

    while heap:
        d, u = heapq.heappop(heap)  

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[D] == float('inf'): 
        print(-1)
        return
    
    print(dist[D])  

    path = []
    curr = D       
    while curr != -1:
        path.append(curr)
        curr = prev[curr]

    path.reverse()
    print(*path)

solve()