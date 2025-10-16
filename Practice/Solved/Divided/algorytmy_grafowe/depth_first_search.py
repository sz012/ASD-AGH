#O(V + E) czas
#O(V) pamiec
'''
Opis:
Przeszukiwanie grafu w głąb. Odwiedza wierzchołek i rekurencyjnie odwiedza jego nieodwiedzonych sąsiadów. Z UJEMNYMI

Zastosowanie:
Sprawdzanie spójności grafu, cykli, topologiczne sortowanie, rozwiązywanie labiryntów.
'''
from collections import deque
#graph - slownik/hashmap sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
def dfsOG(graph, start):
    visited = []
    stack = deque()

    stack.append(start)
    visited.append(start)

    while stack:
        s = stack.pop()
        print(s, end = ' ')

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)
    return visited

def dfs(graph, start, visited=None):
    """
    graph - słownik (dict) sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
    start - wierzchołek początkowy
    visited - zbiór odwiedzonych wierzchołków (na początku None)

    Funkcja wypisuje wszystkie odwiedzone wierzchołki w kolejności DFS
    """

    # 1. Inicjalizujemy zbiór odwiedzonych, jeśli to pierwsze wywołanie
    if visited is None:
        visited = set()

    # 2. Oznaczamy bieżący wierzchołek jako odwiedzony
    visited.add(start)
    print("Odwiedzam:", start)

    # 3. Odwiedzamy rekurencyjnie wszystkich nieodwiedzonych sąsiadów
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    # 4. Zwracamy zbiór odwiedzonych wierzchołków
    return visited


from collections import defaultdict

def dfs_edges(edges, V, start):
    # Tworzenie listy sąsiedztwa
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * V

    def dfs(u):
        visited[u] = True
        print(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)

# Przykład
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
dfs_edges(edges, 4, 0)

def dfs_adj_list(graph, start):
    visited = set()

    def dfs(u):
        visited.add(u)
        print(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)

    dfs(start)

# Przykład
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
dfs_adj_list(graph, 0)

def dfs_matrix(matrix, start):
    V = len(matrix)
    visited = [False] * V

    def dfs(u):
        visited[u] = True
        print(u)
        for v in range(V):
            if matrix[u][v] and not visited[v]:
                dfs(v)

    dfs(start)

# Przykład
matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
dfs_matrix(matrix, 0)
