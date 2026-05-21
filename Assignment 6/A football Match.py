from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    ans = 0

    for start in range (1, n + 1):
        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0
        count = [0, 0]
        count[0] += 1
        is_bipartite = True

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    count[color[v]] += 1
                    q.append(v)
                elif color[v] == color[u]:
                    is_bipartite = False

        if is_bipartite:
            ans += max(count[0], count[1])
        else:
            ans += count[0] + count[1]
    print(ans)

solve()
