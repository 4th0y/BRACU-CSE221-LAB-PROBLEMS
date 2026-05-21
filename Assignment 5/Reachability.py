import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1

def solve():
    n, m, q = map(int, input().split())

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        union(parent, rank, u, v)

    out = []
    for _ in range(q):
        x, y = map(int, input().split())
        out.append("YES" if find(parent, x) == find(parent, y) else "NO")

    print('\n'.join(out))

solve()