from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def solve():
    line = input().split()
    n, A, B = int(line[0]), line[1], line[2]

    words = []
    for _ in range(n):
        words.append(input().strip())

    letter_graph = defaultdict(set)
    word_set = set(words)

    for w in words:
        letter_graph[w[0]].add(w[-1])

    if A == B:
        print("YES")
        return

    if B not in word_set:
        print("NO")
        return

    start = A[-1]
    target = B[0]


    if target == start or target in letter_graph[start]:
        pass

    visited = set([start])
    q = deque([start])

    found = False

    if start == target:
        found = True

    while q and not found:
        ch = q.popleft()
        for nxt in letter_graph[ch]:
            if nxt == target:
                found = True
                break
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    print("YES" if found else "NO")

solve()