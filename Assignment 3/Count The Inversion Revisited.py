import sys
import bisect
input = sys.stdin.readline

n = int(input())
l1 = list(map(int, input().split()))

count = 0
seen_squares = []

for i in range(n - 1, -1, -1):
    idx = bisect.bisect_left(seen_squares, l1[i])
    count += idx
    bisect.insort(seen_squares, l1[i])

print(count)