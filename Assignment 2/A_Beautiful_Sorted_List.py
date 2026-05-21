
import sys
 
input = sys.stdin.readline
 
m = int(input())
l1 = list(map(int, input().split()))
 
n = int(input())
l2 = list(map(int, input().split()))
 
a = []
i = j = 0
 
while i < m and j < n:
    if l1[i] <= l2[j]:
        a.append(l1[i])
        i += 1
    else:
        a.append(l2[j])
        j += 1
 
a.extend(l1[i:])
a.extend(l2[j:])
 
sys.stdout.write(" ".join(map(str, a)))