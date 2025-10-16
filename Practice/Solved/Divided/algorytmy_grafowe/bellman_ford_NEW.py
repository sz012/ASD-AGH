'''
O(V*E) czas O(V) pamiec
Algorytm z tym samym zastosowaniem co algorytm Dijkstry
Tak samo sluzy do znajdowania najkrotszych sciezek miedzy konkretnymi wierzcholkami w grafie
Roznica jest natomiast taka ze moze zostac wykorzystany przy ujemnych wagach krawedzi
Nie dziala jednak przy grafie z ujemnym cyklem
Na koncu kodu kontrolujemy czy takowy nie wystepuje, jesli przejdziemy po grafie
wiecej razy niz posiada wierzcholkow, zwracamy blad
Jest to algorytm wykorzystywany w programowaniu dynamicznym
'''

#graph - słownik sąsiedztwa: {wierzchołek: [(sąsiad, waga), ...]}
#start - wierzcholek poczatkowy
def bellman_ford(graph, start):
    V = len(graph)
    distances = [float('inf')] * V
    distances[start] = 0

    for i in range(V - 1):
        updated = False
        for u in range(V):
            for v, w in graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    updated = True
        if not updated:
            break

    for u in range(V):
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:
                print("Cykl o ujemnej wadze")
                return None

    return distances

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(bellman_ford(graph, 0))