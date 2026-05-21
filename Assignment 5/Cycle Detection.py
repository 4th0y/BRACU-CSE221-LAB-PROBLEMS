import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(2 * 100000 + 5)

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[v].append(u)
    color = [0] * (n + 1)

    def dfs(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1:
                return True
            if color[v] == 0:
                if dfs(v):
                    return True
        color[u] = 2
        return False
    
    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i):
                print("YES")
                return
    print("NO")
solve()