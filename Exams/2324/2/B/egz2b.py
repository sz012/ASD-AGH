'''
Szymon Pytel
Zadanie polega na zaimplementowaniu klasycznej dijkstry gdzie szczegolna uwage zwracamy na krawedzie
i w zaleznosci od tego jaka przeszlismy ostatnio oraz jaka jest przed nami, dodajemy wartosci do kosztu wierzcholka
Wobec tego w kolejce zapisuje poza indeksem wierzcholka i jego cena, rowniez typ ostatnio przebytej sciezki
'''
from egz2btesty import runtests
from collections import defaultdict
import heapq

def dijkstra_modified(graph, start):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  queue = [(0, start, 'A')]

  while queue:
    current_distance, current_node, current_type = heapq.heappop(queue)

    if distances[current_node] < current_distance:
      continue

    for neighbor, weight, type in graph[current_node]:
      distance = current_distance + weight
      if current_type == 'A':
        distance += 0
      elif current_type != type:
        distance += 20
      elif type == 'P':
        distance += 10
      elif type == 'I':
        distance += 5

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(queue, (distance, neighbor, type))

  return distances


def tory_amos( E, A, B ):
  graph = defaultdict(list)
  for u, v, w, t in E:
    graph[u].append((v, w, t))
    graph[v].append((u, w, t))
  distances_result = dijkstra_modified(graph, A)
  return distances_result[B]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
