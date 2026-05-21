from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        print(0)
        return
    
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    dist[x1][y1] = 0
    q = deque([(x1, y1)])

    while q:
        x, y = q.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                if nx == x2 and ny == y2:
                    print(dist[nx][ny])
                    return
                q.append((nx, ny))
    print(-1)

solve()