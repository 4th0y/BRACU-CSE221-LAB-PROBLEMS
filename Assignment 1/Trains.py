import merge_sort as ms

n = int(input())
k = []

for _ in range(n):
    k.append(input().split())

# Sort by time first (secondary), then by flight name (primary)
k = ms.merge_sort(k, key=lambda x: x[-1])
k = ms.merge_sort(k, key=lambda x: x[0])

for row in k:
    print(" ".join(row))