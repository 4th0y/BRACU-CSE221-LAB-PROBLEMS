n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}

left = 0
max_length = 0

for right in range(n):
    num = arr[right]

    count[num] = count.get(num, 0) + 1

    while len(count) > k:
        left_num = arr[left]
        count[left_num] -= 1
        if count[left_num] == 0:
            del count[left_num]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)