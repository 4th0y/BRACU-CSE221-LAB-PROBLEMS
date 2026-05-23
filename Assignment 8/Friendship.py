import sys
input = sys.stdin.readline
 
def solve():
    N, K = map(int, input().split())
    parent = list(range(N + 1))
    size = [1] * (N + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return size[ra]
        
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return size[ra]
    
    out = []
    for _ in range(K):
        a, b = map(int, input().split())
        out.append(union(a, b))

    print('\n'.join(map(str, out)))

solve()