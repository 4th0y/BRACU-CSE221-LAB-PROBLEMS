from collections import deque

def bfs(graph, start, n):
    visited = [False] * (n + 1)

    result = []
    queue = deque()

    visited[start] = True
    queue.append(start)          

    while queue:
        u = queue.popleft()      
        result.append(u)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = bfs(graph, 1, n)
print(*order)