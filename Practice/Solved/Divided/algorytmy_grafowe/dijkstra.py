#O(E + V * logV) czas
#O(V) pamiec
'''
Opis:
Znajduje najkrótsze ścieżki z jednego wierzchołka do pozostałych w grafie z nieujemnymi wagami. BEZ UJEMNYCH

Zastosowanie:
Najkrótsze ścieżki w grafach bez ujemnych wag, np. w mapach i systemach nawigacyjnych.
'''
import heapq  # do kolejki priorytetowej

def dijkstra(graph, start):
    """
    graph - słownik sąsiedztwa: {wierzchołek: [(sąsiad, waga), ...]}
    start - wierzchołek początkowy

    Zwraca: słownik najkrótszych odległości od startu do każdego wierzchołka
    """

    # 1. Inicjalizacja: odległość do każdego wierzchołka to nieskończoność
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # odległość do siebie samego to 0

    # 2. Kolejka priorytetowa przechowująca (dystans, wierzchołek)
    queue = [(0, start)]  # zaczynamy od startu z dystansem 0

    # 3. Pętla główna
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 4. Jeśli znaleźliśmy już krótszą ścieżkę wcześniej — pomijamy
        if current_distance > distances[current_node]:
            continue

        # 5. Sprawdzamy sąsiadów aktualnego wierzchołka
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 6. Jeśli znaleźliśmy krótszą ścieżkę do sąsiada — aktualizujemy
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # 7. Zwracamy słownik najkrótszych odległości
    return distances


from collections import defaultdict

def dijkstra_edges(edges, V, start):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [float('inf')] * V
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

# Przykład
edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
print(dijkstra_edges(edges, 4, 0))

def dijkstra_adj_list(graph, V, start):
    dist = [float('inf')] * V
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

# Przykład
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra_adj_list(graph, 4, 0))

import heapq

def dijkstra_matrix(matrix, start):
    V = len(matrix)
    dist = [float('inf')] * V
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v in range(V):
            if matrix[u][v] != float('inf') and dist[u] + matrix[u][v] < dist[v]:
                dist[v] = dist[u] + matrix[u][v]
                heapq.heappush(heap, (dist[v], v))

    return dist

# Przykład
INF = float('inf')
matrix = [
    [0, 4, 1, INF],
    [INF, 0, INF, 1],
    [INF, 2, 0, 5],
    [INF, INF, INF, 0]
]
print(dijkstra_matrix(matrix, 0))
