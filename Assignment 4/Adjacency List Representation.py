class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))

n, m = map(int, input().split())
g = Graph(n)
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(m):
    g.add_edge(u[i]-1, v[i]-1, w[i])

for i in range(n):
    print(f"{i+1}: ", end="")
    for (neighbor, weight) in g.adj_list[i]:
        print(f"({neighbor+1},{weight})", end=" ")
    print()