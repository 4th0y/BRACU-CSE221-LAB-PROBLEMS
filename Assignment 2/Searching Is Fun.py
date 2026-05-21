t = int(input())
for _ in range(t):
    k, x = map(int, input().split())
    full_groups = k // (x - 1)
    remainder = k % (x - 1)
    ans = full_groups * x + remainder

    if remainder == 0:
        ans -= 1
        
    print(ans)