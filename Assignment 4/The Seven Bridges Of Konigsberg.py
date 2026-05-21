n, m = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (n + 1)
for i in range(m):
    degree[u[i]] += 1
    degree[v[i]] += 1


odd_count = sum(1 for i in range(1, n + 1) if degree[i] % 2 == 1)

if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")