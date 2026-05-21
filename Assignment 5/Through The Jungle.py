from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, end, n):
    parent = [-1] * (n + 1)

    parent[start] = 0

    queue = deque([start])

    while queue:
        u = queue.popleft()

        if u == end:
            break

        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                queue.append(v)

    if parent[end] == -1:
        return None
    
    path = []
    curr = end
    while curr != 0:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path

def solve():
    n, m, s, d, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        reverse_graph[v].append(u)

    path_sk = bfs(graph, s, k, n)
    path_kd = bfs(reverse_graph, d, k, n)

    if path_sk is None or path_kd is None:
        print(-1)
        return
    
    path_kd.reverse()

    full_path = path_sk + path_kd[1:]

    print(len(full_path) - 1)
    print(*full_path)

solve()