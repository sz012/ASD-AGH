'''
O(V+E) czas O(V) pamiec
Algorytm przeszukujacy graf wszerz
Odwiedza wierzcholki poziomamim zaczynajac od startowego
NIE mozna stosowac z wartosciami UJEMNYMI
Sluzy do znajdowania najkrotszej sciezki w grafie bez wag, znajdowania komponentow spojnych
Uzywa kolejki FIFO (first in first out)
'''

#graph - słownik/hashmap sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    order = []

    while queue:
        s = queue.popleft()
        order.append(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(bfs(graph, 0))