import bisect

def range_subArray(arr, l, r):
    left_index = bisect.bisect_left(arr, l)   
    right_index = bisect.bisect_right(arr, r)
    return right_index - left_index

n, q = map(int, input().split())
arr = list(map(int, input().split()))

res = []

for _ in range(q):
    l, r = map(int, input().split())
    res.append(range_subArray(arr, l, r))

for i in res:
    print(i)
