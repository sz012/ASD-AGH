def edge_list_to_adj_list(edge_list):
    max_vertex = max(max(u, v) for u, v in edge_list)
    n = max_vertex + 1  # numeracja od 0

    adj = [[] for _ in range(n)]
    for u, v in edge_list:
        adj[u].append(v)
        adj[v].append(u)  # dodaj drugą stronę dla nieskierowanego grafu
    return adj

def matrix_to_adj_list(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u].append([v, graph[u][v]])
                new_graph[v].append([u, graph[u][v]])

    return new_graph

