import sys
from math import log2
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    edges = []
    for i in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v, i))
    
    edges.sort()
    
    # ── Kruskal's MST ──────────────────────────────────────────────
    parent = list(range(N + 1))
    sz = [1] * (N + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if sz[a] < sz[b]: a, b = b, a
        parent[b] = a
        sz[a] += sz[b]
        return True

    mst_weight = 0
    in_mst = [False] * M          # which edges are in MST
    adj = [[] for _ in range(N + 1)]  # MST adjacency list

    for idx, (w, u, v, eid) in enumerate(edges):
        if union(u, v):
            mst_weight += w
            in_mst[eid] = True
            adj[u].append((v, w))
            adj[v].append((u, w))

    # ── Binary Lifting for LCA + path-max query ────────────────────
    LOG = max(1, int(log2(N)) + 1)

    depth  = [0] * (N + 1)
    up     = [[0] * (N + 1) for _ in range(LOG)]   # ancestor
    maxW   = [[0] * (N + 1) for _ in range(LOG)]   # max edge weight on path to ancestor

    # BFS to set up depth, parent, direct edge weight
    from collections import deque
    visited = [False] * (N + 1)
    q = deque([1])
    visited[1] = True
    while q:
        node = q.popleft()
        for nei, w in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                depth[nei] = depth[node] + 1
                up[0][nei] = node
                maxW[0][nei] = w
                q.append(nei)

    # Fill binary lifting table
    for k in range(1, LOG):
        for v in range(1, N + 1):
            up[k][v]   = up[k-1][up[k-1][v]]
            maxW[k][v] = max(maxW[k-1][v], maxW[k-1][up[k-1][v]])

    def query_max(u, v):
        """Max edge weight on path u→v in MST (LCA-based)."""
        res = 0
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                res = max(res, maxW[k][u])
                u = up[k][u]
        if u == v:
            return res
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                res = max(res, maxW[k][u], maxW[k][v])
                u, v = up[k][u], up[k][v]
        res = max(res, maxW[0][u], maxW[0][v])
        return res

    # ── Try every non-MST edge ─────────────────────────────────────
    ans = float('inf')
    for w, u, v, eid in edges:
        if in_mst[eid]:
            continue
        path_max = query_max(u, v)
        if w > path_max:                        # strict increase guaranteed
            ans = min(ans, mst_weight - path_max + w)

    print(ans if ans != float('inf') else -1)

main()