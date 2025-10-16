'''
Szymon Pytel
Wierzcholki grafu wazonego nieskierowanego to zamki, a krawedzie to drogi miedzy nimi
Zlycerz musi przejsc od s do t i jak najmniej zaplacic badz jak najwiecej zyskac
Mozemy obrabowac maksymalnie jeden zamek, przy czym w takim wypadku kazda kolejna krawedz
ma podwojony koszt oraz za kazda krawedz placimy lapowke r
Co wazne, zwracamy koszt, a nie zysk, wiec jesli zyskujemy zwracamy liczbe ujemna
Wobec tego musimy znalezc jak NAJMNIEJSZY koszt
Moim pomyslem jest na poczatku jednorazowo przez dijkstre okreslic odleglosci do zamkow,
a nastepnie (NIE: dla kazdego zamku odpalic ja jeszcze raz i na biezaco porownywac)
(TAK: odpalic ja od konca znowu tylko raz dla lepszej zlozonosci i wyciagac odleglosci po indeksach zamkow)
Po drodze zaaktualizujemy graf gdyz po kradziezy kazda droga wydluza sie razy 2
i zwieksza o stala r, robimy to PRZED czescia z zamkami
'''
from egz1Atesty import runtests
from collections import defaultdict
import heapq

def graph_change(G):
  graph = defaultdict(list)
  for u in range(len(G)):
    graph[u].append(G[u])
    graph[u] = graph[u][0]
  return graph

def dijkstra(graph, start):
  #distances = {node: float('inf') for node in graph}

  distances = [float("inf") for _ in range(len(graph))]
  distances[start] = 0

  queue = [(0, start)]
  while queue:
    cur_dist, cur_node = heapq.heappop(queue)

    if cur_dist > distances[cur_node]:
      continue

    for neighbor, weight in graph[cur_node]:
      distance = cur_dist + weight

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(queue, (distance, neighbor))
  return distances

def gold(G,V,s,t,r):
  #graph = graph_change(G)

  first_distances = dijkstra(G, s)
  min_distance = first_distances[t]

  for a in range(len(G)):
    for b in range(len(G[a])):
      modified_tuple = (G[a][b][0], (G[a][b][1] * 2) + r)
      G[a][b] = modified_tuple
  #graph = graph_change(G)

  new_distances = dijkstra(G, t)
  for i in range(len(V)):
    new_distance = first_distances[i] + new_distances[i] - V[i]
    min_distance = min(min_distance, new_distance)
  return min_distance


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = False )
