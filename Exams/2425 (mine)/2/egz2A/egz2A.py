'''
Szymon Pytel
Moim pomyslem jest poczatkowo zmieniajac reprezentacje grafu na zgodna z DFSem
wykonywac go w petli - startujac z pozycji krola szukac pozycji krolowej
i pomijac wierzcholki zblokowane przez bajtocje
Aby lekko przyspieszyc dzialanie algorytmu funkcja DFS zamiast zwracac 'order'
ktory nalezy pozniej przeszukac konczy swoje dzialanie i zwraca True gdy znajdzie pozycje krolowej
Zlozonosc rozwiazania to O(D(V+E))
'''
from egz2Atesty import runtests
from collections import deque

def dfs_modified(graph, start, exc, finish):
    visited = set()
    stack = deque()

    visited.add(start)
    stack.append(start)

    order = []

    while stack:
        s = stack.pop()
        order.append(s)
        for neighbor in reversed(graph[s]):
            if neighbor == finish:
                return True
            if neighbor not in visited and neighbor != exc:
                visited.add(neighbor)
                stack.append(neighbor)

    return False

def graph_change(V, E):
    graph = [[] for _ in range(V)]

    for i in range(len(E)):
        graph[E[i][0]].append(E[i][1])
        graph[E[i][1]].append(E[i][0])

    return graph

def kingnqueen( V,E,D,K,Q,B ):
  graph = graph_change(V, E)
  res = 0
  for d in range(D):
      cur_res = dfs_modified(graph, K[d], B[d], Q[d])
      res += cur_res
  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kingnqueen, all_tests = False )
