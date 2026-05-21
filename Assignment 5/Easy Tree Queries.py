import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    size = [1] * (n + 1)
    parent = [0] * (n + 1)
    order = []

    visited = [False] * (n + 1)
    stack = [r]
    visited[r] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)
    for u in reversed(order):
        if parent[u] != 0:
            size[parent[u]] += size[u]

    q = int(input())
    out = []
    for _ in range(q):
        x = int(input())
        out.append(str(size[x]))

    print('\n'.join(out))
solve()