'''
O(E+V*logV) czas O(V) pamiec
Dijkstra to prawdopodobnie najpopularniejszy algorytm sluzacy do znajdowania
najkrotszych drog miedzy konkretnymi wierzcholkami w grafie z nieujemnymi wagami krawedzi
Wykorzystywany jest przykladowo w nawigacji
Jest to algorytm zachlanny
'''

#graph - słownik sąsiedztwa: {wierzchołek: [(sąsiad, waga), ...]}
#start - wierzcholek poczatkowy
import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)

        if currentDistance > distances[currentNode]:
            continue

        for neighbor, weight in graph[currentNode]:
            distance = currentDistance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra(graph, 0))

