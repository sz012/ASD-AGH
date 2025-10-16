'''
Szymon Pytel

Dobrycerz szuka najmniej kosztownej drogi z punktu s do punktu t w grafie nieskierowanym
przy czym bez snu moze przebyc maksymalnie 16 jednostek. Krawedzie maja maksymalnie po 8
a jezeli rycerz zatrzymuje sie na nocleg to kosztuje go to 8 jednostek.
Moim pomyslem jest zastosowac algorytm dijkstry w najprostszej postaci i
w rezultacie go pozniej przywolujac, po znalezieniu najkrotszej sciezki dodac do niej ilosc noclegow
na jakie zatrzymal sie rycerz

ZLE bo jeden test nie przechodzi - trzeba zmodyfikowac dijkstre aby liczyla na biezaco
czas od ostatniego noclegu
'''

from egz3atesty import runtests
import heapq

def matrix_to_adj_list(G):
  n = len(G)
  graph = [[] for _ in range(n)]

  for u in range(n):
    for v in range(n):
      if G[u][v] != -1:
        graph[u].append([v, G[u][v]])
        graph[v].append([u, G[u][v]])
  return graph

def dijkstra(graph, start):
  distances = [float('inf') for node in graph]
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

def goodknight( G, s, t ):
  res = dijkstra(matrix_to_adj_list(G), s)
  return res[t] + (res[t]//16 * 8)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
