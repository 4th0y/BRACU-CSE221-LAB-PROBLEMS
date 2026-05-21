class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.degree = [0] * vertices

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.degree[u] += 1
        self.degree[v] += 1

v, e = map(int, input().split())
g = Graph(v)
u_nodes = list(map(int, input().split()))
v_nodes = list(map(int, input().split()))

for i in range(e):
    g.add_edge(u_nodes[i] - 1, v_nodes[i] - 1)

for i in range(v):
    out_degree = len(g.adj_list[i])
    in_degree = g.degree[i] - out_degree
    print(-out_degree + in_degree, end=" ") 