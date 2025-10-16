'''
O(V+E) czas O(V) pamiec
Algorytm preszukujacy graf wglab
Odwiedza wierzcholek i rekurencyjnie jego nieodwiedzonych sasiadow
Mozna stosowac z wartosciami UJEMNYMI
Sluzy do sprawdzania spojnosci grafu, cykli, topologicznego sortowania czy rozwiazywania labiryntow
Uzywa kolejki LIFO (last in first out)
'''

#graph - slownik/hashmap sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
#iteracja, wolniejsze ale bezpieczniejsze
from collections import deque
def dfs(graph, start):
    visited = set()
    stack = deque()

    visited.add(start)
    stack.append(start)

    order = []

    while stack:
        s = stack.pop()
        order.append(s)
        for neighbor in reversed(graph[s]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order

#graph - slownik/hashmap sąsiedztwa: {wierzchołek: [lista_sąsiadów]}
#rekurencja, szybsze ale ryzykowne dla duzych grafow
def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()

    order = []

    if start not in visited:
        order.append(start)
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                order.extend(dfs2(graph, neighbor, visited))

    return order

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(dfs(graph, 0))