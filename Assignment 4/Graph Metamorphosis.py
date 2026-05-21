n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    k = row[0]
    neighbors = row[1:]
    for j in neighbors:
        matrix[i][j] = 1

for row in  matrix:
    print(*row)

    