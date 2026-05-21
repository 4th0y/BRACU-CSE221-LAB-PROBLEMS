import sys
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = {v: i for i, v in enumerate(inorder)}

result = []

def build(in_l, in_r, post_l, post_r):
    if in_l > in_r:
        return     
        # traversal completed

    root = postorder[post_r]
    idx = pos[root]

    left_size = idx -in_l

    result.append(root)

    build(in_l, idx - 1, post_l, post_l + left_size - 1)
    build(idx + 1, in_r, post_l + left_size, post_r - 1)

build(0, n - 1, 0, n - 1)

print(*result)