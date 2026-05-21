from collections import deque
import sys
input = sys.stdin.readline

def solve():
    S, C = input().split()      
    n = int(input())
    forbidden = set()
    for _ in range(n):
        forbidden.add(input().strip())

    if C in forbidden:
        print(-1)
        return
    
    if S == C:
        print(0)
        return
    
    dist = {S: 0}
    q = deque([S])

    while q:
        curr = q.popleft()
        for i in range(4):
            for delta in (-1, 1):
                lst = list(curr)
                lst[i] = str((int(lst[i]) + delta) % 10) 
                nxt = ''.join(lst)
                if nxt not in forbidden and nxt not in dist: 
                    dist[nxt] = dist[curr] + 1
                    if nxt == C:
                        print(dist[nxt])
                        return
                    q.append(nxt)

    print(-1)

solve()