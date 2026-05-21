n = int(input())
x, y = map(int, input().split())

moves = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
            continue
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            moves.append((nx, ny))

moves.sort()

print(len(moves))
for a, b in moves:
    print(a, b)