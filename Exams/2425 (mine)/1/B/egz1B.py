'''
Szymon Pytel
Zadaniem programu jest policzyc ilosc delegacji (krawedzi) krytycznych, czyli takich, po ktorych usunieciu
co najmniej jeden wierzcholek jest nieosiagalny
Moim pomyslem jest wykorzystac do zadania algorytm BFS, ktory w petli bedziemy wykorzystywac dla
kazdego wierzcholka uprzednio usuwajac poszczegolne krawedzie
Jesli len(new_order) < len(old_order), oznacza to ze krawedz jest krytyczna bo w BFS-ie nie udalo nam sie dojsc do wszystkich wierzcholkow

'''
from egz1Btesty import runtests
from collections import deque
from collections import defaultdict

def graph_change(E):
    graph = defaultdict(list)
    for i in range(len(E)):
        graph[E[i][0]].append(E[i][1])
    return graph

def bfs_modified(graph, start, deleted):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)
    order = []

    while queue:
        s = queue.popleft()
        order.append(s)

        for neighbor in graph[s]:
            if (s, neighbor) == deleted:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def critical(V, E):
    graph = graph_change(E)

    ctr = 0
    for e in E:
        v = 0
        while v <= V:
            old_order = bfs_modified(graph, v, None)
            new_order = bfs_modified(graph, v, e)
            if len(new_order) < len(old_order):
                ctr += 1
                break
            v += 1
    return ctr

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = False)
