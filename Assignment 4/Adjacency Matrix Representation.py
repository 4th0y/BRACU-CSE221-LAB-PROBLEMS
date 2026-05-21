class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj_matrix[u][v] = w


n, m = map(int, input().split())
g = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    g.add_edge(u - 1, v - 1, w)

for row in g.adj_matrix:
    print(*row)
    