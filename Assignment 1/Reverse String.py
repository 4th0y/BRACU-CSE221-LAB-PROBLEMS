n = int(input())
a = list(map(int, input().split()))

if n <= 2:
    print("YES")
    print(0)
else:
    ops = []
    for _ in range(n * n):  
        swapped = False
        for i in range(n - 2):
            if a[i] > a[i + 2]:
                a[i], a[i + 2] = a[i + 2], a[i]
                ops.append((i + 1, i + 3))
                swapped = True
        
        if not swapped:
            break
    is_sorted = all(a[i] <= a[i + 1] for i in range(n - 1))
    
    if is_sorted:
        print("YES")
        print(len(ops))
        for op in ops:
            print(*op)
    else:
        print("NO")