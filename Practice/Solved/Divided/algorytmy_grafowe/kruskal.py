#O(E * logE) czas
#O(V) pamiec
'''
Opis:
Znajduje minimalne drzewo rozpinające (MST). Sortuje krawędzie i dodaje je do drzewa, jeśli nie tworzą cyklu. Z UJEMNYMI

Zastosowanie:
Budowa najtańszych sieci (np. połączenia komputerów, dróg).
'''
def find(parent, x):
    """
    Funkcja 'find' znajduje reprezentanta zbioru (z kompresją ścieżki).
    """
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # kompresja ścieżki
    return parent[x]


def union(parent, rank, x, y):
    """
    Funkcja 'union' łączy dwa zbiory w jeden (z użyciem rangi).
    """
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False  # już są w tym samym zbiorze

    # Union by rank – dołącz mniejsze drzewo do większego
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    return True


def kruskal(n, edges):
    """
    Algorytm Kruskala dla grafu o n wierzchołkach i liście krawędzi.

    edges - lista krawędzi (waga, u, v)
    n - liczba wierzchołków (numerowane od 0 do n-1)

    Zwraca: sumę wag MST i listę krawędzi tworzących MST
    """

    # 1. Posortuj krawędzie według wagi rosnąco
    edges.sort()

    # 2. Inicjalizacja struktur zbiorów rozłącznych (Union-Find)
    parent = list(range(n))  # każdy wierzchołek to osobny zbiór
    rank = [0] * n

    mst_weight = 0  # suma wag MST
    mst_edges = []  # lista krawędzi w MST

    # 3. Przechodzimy po posortowanych krawędziach
    for weight, u, v in edges:
        if union(parent, rank, u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            # Jeśli już mamy n-1 krawędzi, przerywamy (drzewo pełne)
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges


def kruskal_edges(edges, V):
    # Sortowanie krawędzi rosnąco według wagi
    edges.sort(key=lambda x: x[2])
    parent = list(range(V))

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        parent[find(u)] = find(v)

    mst = []
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst

# Przykład
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]
print(kruskal_edges(edges, 4))

def kruskal_adj_list(graph, V):
    edges = []
    added = set()
    for u in graph:
        for v, w in graph[u]:
            if (v, u) not in added:
                edges.append((u, v, w))
                added.add((u, v))

    return kruskal_edges(edges, V)

# Przykład
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}
print(kruskal_adj_list(graph, 4))

def kruskal_matrix(matrix):
    V = len(matrix)
    edges = []
    for u in range(V):
        for v in range(u + 1, V):  # tylko górny trójkąt (graf nieskierowany)
            if matrix[u][v] != float('inf'):
                edges.append((u, v, matrix[u][v]))

    return kruskal_edges(edges, V)

# Przykład
INF = float('inf')
matrix = [
    [0,   4,   3,   INF],
    [4,   0,   1,   2],
    [3,   1,   0,   4],
    [INF, 2,   4,   0]
]
print(kruskal_matrix(matrix))
