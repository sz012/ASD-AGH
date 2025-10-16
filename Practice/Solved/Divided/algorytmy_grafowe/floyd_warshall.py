#O(V^3) czas
#O(V^2) pamiec
'''
Opis:
Algorytm służy do znajdowania najkrótszych ścieżek pomiędzy wszystkimi parami wierzchołków w grafie skierowanym lub nieskierowanym.
Obsługuje ujemne wagi, ale nie może być cyklu o ujemnej wadze. Z UJEMNYMI

Zastosowanie:
Użyteczny, gdy potrzebujemy znać najkrótsze ścieżki między każdą parą wierzchołków
np. w analizie połączeń w sieciach, transporcie, analizie zależności.
'''


def floyd_warshall_edges(edges, V):
    INF = float('inf')
    dist = [[INF] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Przykład
edges = [(0, 1, 3), (0, 2, 8), (1, 2, 2), (2, 0, 5)]
print(floyd_warshall_edges(edges, 3))


def floyd_warshall_adj_list(graph, V):
    INF = float('inf')
    dist = [[INF] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Przykład
graph = {
    0: [(1, 3), (2, 8)],
    1: [(2, 2)],
    2: [(0, 5)]
}
print(floyd_warshall_adj_list(graph, 3))

def floyd_warshall_matrix(matrix):
    V = len(matrix)
    dist = [row[:] for row in matrix]  # Kopia macierzy

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Przykład
INF = float('inf')
matrix = [
    [0,   3,   8],
    [INF, 0,   2],
    [5,   INF, 0]
]
print(floyd_warshall_matrix(matrix))
