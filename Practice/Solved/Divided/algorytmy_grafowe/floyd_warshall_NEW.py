'''
O(n^3) czas O(n^2) pamiec
Algorytm floyda-warshalla ma podobne zastosowanie do dijkstry i bellmana-forda
Wyszukuje on natomiast najkrotsze drogi miedzy kazda mozliwa para wierzcholkow
za co placimy duza zlozonoscia
Kod opiera sie na trzech petlach ktore progresywnie zmieniaja wartosci w tablicy o wymiarach
u x v (kwadratowej) gdzie kazda komorka oznacza najkrotsza sciezke od wierzcholka u do v
'''

#graph - słownik sąsiedztwa: {wierzchołek: [(sąsiad, waga), ...]}
def floyd_warshall(graph):
    nodes = list(graph.keys())

    distances = {u: {v: float('inf') for v in nodes} for u in nodes}

    for u in nodes:
        distances[u][u] = 0

    for u in graph:
        for v in graph[u]:
            distances[u][v] = graph[u][v]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

graph = {
    'A': {'B': 3, 'C': 8},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 4},
}
print(floyd_warshall(graph))

