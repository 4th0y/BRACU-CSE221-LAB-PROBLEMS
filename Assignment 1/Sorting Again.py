test_case = int(input())
for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))   # IDs
    b = list(map(int, input().split()))   # Marks
    ab = list(zip(a, b))                  # Pair them

    count = 0
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if ab[j][1] > ab[max_index][1] or (ab[j][1] == ab[max_index][1] and ab[j][0] < ab[max_index][0]):
                max_index = j
        if max_index != i:
            ab[i], ab[max_index] = ab[max_index], ab[i]
            count += 1

    print(f"Minimum swaps: {count}")
    for id_, mark in ab:
        print(f"ID: {id_} Mark: {mark}")