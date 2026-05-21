import sys
sys.setrecursionlimit(2 * 100000 + 5)

def dfs(graph, u, visited, result):
    visited[u] = True
    result.append(u)

    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited, result)

#====read input=============================================
input_data = sys.stdin.read().split()
idx = 0

n = int(input_data[idx]); idx += 1  #no. of roads
m = int(input_data[idx]); idx += 1 #no. of cities

u_nodes = []
for _ in range(m):
    u_nodes.append(int(input_data[idx])); idx += 1


v_nodes = []
for _ in range(m):
    v_nodes.append(int(input_data[idx])); idx += 1


#============== Build Adjacency List  ==========================
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u = u_nodes[i]
    v = v_nodes[i]
    graph[u].append(v)
    graph[v].append(u)

#============== Run DFS From Node 1 ============================

visited  = [False] * (n + 1)
result = []

dfs(graph, 1, visited, result)

#============== result ================================
print(*result)