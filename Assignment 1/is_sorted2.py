import Merge_Sort2 as ms2
n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(str,input().split()))
    arr=ms2.merge_sort2(l)
    if arr==l:
        print("YES")
    else:
        print("NO")
    