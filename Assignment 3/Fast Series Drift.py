import sys
input = sys.stdin.readline

def solve(a, n, m):
    if n == 0:
        return 0
    
    if n % 2 == 1:
        return (pow(a, n, m) + solve(a, n-1, m)) % m
    
    half = solve(a, n//2, m)
    return(half + pow(a, n//2, m) * half % m) % m

t = int(input())

for _ in range(t):
    a, n, m = map(int, input().split())
    print(solve(a, n, m))