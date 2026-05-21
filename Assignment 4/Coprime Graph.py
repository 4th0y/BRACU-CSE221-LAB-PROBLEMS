import sys
from math import gcd

def build_graph(N):
    neighbors = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if gcd(i, j) == 1:
                neighbors[i].append(j)
                neighbors[j].append(i)

    return neighbors


def answer_queries(neighbors, queries):
    results = []

    for X, K in queries:
        neighbor_list = neighbors[X]
        index = K - 1

        if index < len(neighbor_list):
            results.append(str(neighbor_list[index]))
        else:
            results.append("-1")

    return results


def solve():
    try:
        data = sys.stdin.read().split()
        if not data:
            return

        it = iter(data)
        N = int(next(it))
        Q = int(next(it))

        queries = []
        for _ in range(Q):
            X = int(next(it))
            K = int(next(it))
            queries.append((X, K))

    except (StopIteration, Exception):
        return

    neighbors = build_graph(N)
    results = answer_queries(neighbors, queries)
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == "__main__":
    solve()