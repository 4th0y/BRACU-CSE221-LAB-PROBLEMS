import sys
input= sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

pos = {v: i for i, v in enumerate(inorder)}

result = []

def build(in_l, in_r, pre_l, pre_r ):
    if in_l > in_r:
        return 
    root = preorder[pre_l]
    idx = pos[root]
    left_size = idx - in_l

    build(in_l, idx - 1, pre_l + 1, pre_l + left_size)
    build(idx + 1, in_r, pre_l + left_size + 1, pre_r)

    result.append(root)

build(0, n - 1, 0, n - 1)

print(*result)



