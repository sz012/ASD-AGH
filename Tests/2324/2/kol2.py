'''
Szymon Pytel
Najszybsza sciezkie miedzy miastami znajde za pomoca algorytmu Bellmana-Forda
Dane podane sa w reprezentacji grafu za pomoca listy krawedziowej
'''
from kol2testy import runtests

def warrior(G, s, t):
    V = max(max(u, v) for u, v, _ in G) + 1  # automatyczne wyznaczenie liczby wierzchołków

    dist = [float('inf')] * V
    dist[s] = 0

    for _ in range(V - 1):
      for u, v, w in G:
        if dist[u] + w < dist[v]:
          dist[v] = dist[u] + w

    return dist[t] + ((dist[t] // 16) * 8) if dist[t] != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )