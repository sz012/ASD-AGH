#O(V + E) czas
#O(V) pamiec
'''
Opis:
Przeszukiwanie grafu wszerz. Odwiedza wierzchołki poziomami, zaczynając od startowego. BEZ UJEMNYCH

Zastosowanie:
Znalezienie najkrótszej ścieżki w grafie bez wag, znajdowanie komponentów spójnych.
'''
from collections import deque
#graph - słownik/hashmap sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
def bfsOG(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end = ' ')

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited



def bfs(graph, start):
    """
    graph - słownik (dict) sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
    start - wierzchołek początkowy

    Funkcja wypisuje wszystkie odwiedzone wierzchołki w kolejności BFS
    """

    # 1. Zbiór odwiedzonych wierzchołków (aby uniknąć cykli i wielokrotnych odwiedzin)
    visited = set()

    # 2. Kolejka do przechowywania wierzchołków do odwiedzenia (FIFO)
    queue = deque()

    # 3. Dodajemy wierzchołek startowy do kolejki i oznaczamy jako odwiedzony
    visited.add(start)
    queue.append(start)

    # 4. Główna pętla BFS
    while queue:
        # 5. Pobierz pierwszy element z kolejki
        vertex = queue.popleft()
        print("Odwiedzam:", vertex)

        # 6. Odwiedź wszystkich sąsiadów
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # oznacz jako odwiedzonego
                queue.append(neighbor)  # dodaj do kolejki

    # 7. Zwróć zbiór odwiedzonych wierzchołków
    return visited


from collections import defaultdict, deque

def bfs_edges(edges, V, start):
    # Tworzenie listy sąsiedztwa
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * V
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        print(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

# Przykład
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
bfs_edges(edges, 4, 0)

from collections import deque

def bfs_adj_list(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        u = queue.popleft()
        print(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)

# Przykład
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
bfs_adj_list(graph, 0)

from collections import deque

def bfs_matrix(matrix, start):
    V = len(matrix)
    visited = [False] * V
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        print(u)
        for v in range(V):
            if matrix[u][v] and not visited[v]:
                visited[v] = True
                queue.append(v)

# Przykład
matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
bfs_matrix(matrix, 0)
