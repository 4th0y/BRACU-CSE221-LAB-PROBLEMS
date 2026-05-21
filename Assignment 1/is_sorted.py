x = int(input())

for _ in range(x):
    y = int(input())
    number = list(map(int, input().split()))
    if number == sorted(number):
        print("YES")
    else:
        print("NO")