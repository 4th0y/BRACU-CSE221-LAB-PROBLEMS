import sys
from collections import deque
input = sys.stdin.readline

def solve():
    r, h = map(int, input().split())
    grid = [input().strip() for _ in range(r)]

    visited = [[False] * h for _ in range(r)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up down left right

    def bfs(sr, sc):
        diamonds = 0
        queue = deque([(sr, sc)])
        visited[sr][sc] = True

        while queue:
            row, col = queue.popleft()

            if grid[row][col] == 'D':
                diamonds += 1               # collect diamond

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # check bounds, not visited, not obstacle
                if 0 <= nr < r and 0 <= nc < h and not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return diamonds

    max_diamonds = 0

    for i in range(r):
        for j in range(h):
            # start BFS from every unvisited, non-obstacle cell
            if not visited[i][j] and grid[i][j] != '#':
                max_diamonds = max(max_diamonds, bfs(i, j))

    print(max_diamonds)

solve()