'''
Szymon Pytel
Zadanie sprowadza sie do naturalnego problemu gdzie szukamy najkrotszej drogi w grafie od startu do mety
Dodatkowa trudnoscia jest to ze w konkretnych wierzcholkach znajduja sie 'rowery', ktore pozwalaja
na skrocenie sobie reszty drogi
Przeksztalcam reprezentacje grafu z listy krawedzi na slownik sasiedztwa poniewaz
nie kosztuje to duzo zlozonosci a na niej wlasnie operuje dijkstra
Poczatkowo stosujemy algorytm dijkstry jeden raz na grafie bez rowerow
Nastepnie od rowerow korzystnych, ponownie dijkstra sprawdzamy droge i oceniamy czy jest lepsza
Kod ma zwrocic koszt najtanszej drogi - sa ta minuty ktore liczy jej przebycie
'''
import math
from egz1atesty import runtests
import heapq
from collections import defaultdict

def dijkstra_modified(graph, start):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  queue = [(0, start)]

  while queue:
    curDist, curNode = heapq.heappop(queue)

    if curDist > distances[curNode]:
      continue

    for neighbor, weight in graph[curNode]:
      distance = curDist + weight

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(queue, (distance, neighbor))

  return distances


def armstrong( B, G, s, t):
  #Przeksztalcenie listy krawedzi na slownik sasiedztwa
  graph = defaultdict(list)
  for u, v, w in G:
    graph[u].append((v, w))
    graph[v].append((u, w))

  # Tworzenie tablicy z korzystnymi rowerami
  bikes = [1 for node in graph]
  for a, b, c in B:
    if b / c < bikes[a]:
      bikes[a] = b / c

  #Zastosowanie zmodyfikowanego algorytmu dijkstry
  distancesMain = dijkstra_modified(graph, s)
  minRes = distancesMain[t]
  for i in range(len(bikes)):
    if bikes[i] < 1:
      distancesNew = dijkstra_modified(graph, i)
      minRes = min(minRes, distancesMain[i] + (distancesNew[t] * bikes[i]))

  return math.floor(minRes)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = False )
