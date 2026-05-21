import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
l = list(map(int, input().split()))

i = 0
j = len(l) - 1

res = None

while( i < j ):
    su = l[i] + l[j]
    if su == n[1]:
        res = [i + 1, j + 1]
        break
    elif su < n[1]:
        i += 1
    else:
        j -= 1
if res:
    print(*res)
else:
    print(-1)