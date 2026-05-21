import sys
 
def solve():
    input = sys.stdin.readline
    
    n, target = map(int, input().split())
    
    arr = list(map(int, input().split()))
    arr = [(arr[i], i + 1) for i in range(n)]
    arr.sort()   
    
    for i in range(n - 2):
    
        if arr[i][0] * 3 > target:
            break
        if arr[i][0] + arr[n-2][0] + arr[n-1][0] < target:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            s = arr[i][0] + arr[left][0] + arr[right][0]
            
            if s == target:
                print(arr[i][1], arr[left][1], arr[right][1])
                return
            elif s < target:
                left += 1
            else:
                right -= 1
    
    print(-1)
 
solve()