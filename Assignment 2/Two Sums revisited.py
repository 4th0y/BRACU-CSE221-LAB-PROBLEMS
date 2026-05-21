import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
i = 0
j = M - 1
rec = [float('inf'), [0, 0]]
 
while i < N and j >= 0:
    add = A[i] + B[j]
    diff = abs(add - K)
    
    if diff < rec[0]:
        rec = [diff, [i + 1, j + 1]]
    
    if add == K:
        break
    elif add < K:
        i += 1
    else:
        j -= 1
 
print(*rec[1])