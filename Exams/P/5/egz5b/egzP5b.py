'''
Szymon Pytel
Program ma za zadanie obliczyc ile w grafie jest dworcow
po ktorych usunieciu bedziemy nadal mogli dotrzec do wszystkich pozostalych
Mamy do czynienia ze specyficzna reprezentacja grafu bo w tablicy B znajduja sie
powtarzajace sie krawedzie miedzy wierzcholkami
Moim pomyslem jest pomijajac powtarzajace sie krawedzie uzyc algorytmu
przeszukiwujacego typu DFS lub BFS za kazdym razem ignorujac krawedzie usunietego dworca
Algorytm ten wyznaczy nam ilosc dworcow spelniajacych warunki zadania
'''
from egzP5btesty import runtests
from collections import deque
from collections import defaultdict

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

def make_graph(graph):
    new_graph = defaultdict(list)
    for i in range(len(graph)):
        new_graph[graph[i][0]].append(graph[i][1])
        new_graph[graph[i][1]].append(graph[i][0])
    return new_graph

def koleje ( B ):
    graph = make_graph(B)
    print(B)
    print(graph)
    return -1

runtests ( koleje, all_tests=False )