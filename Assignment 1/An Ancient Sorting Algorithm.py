n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    swapped=False
    for j in range(0,n-1):
        if (a[j]%2==0 and a[j+1]%2==0) or (a[j]%2!=0 and a[j+1]%2!=0):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
    if not swapped:
        break
print(*a)