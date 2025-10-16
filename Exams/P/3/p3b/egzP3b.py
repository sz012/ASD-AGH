'''
Szymon Pytel
Mamy podany graf w ktorym nalezy pousuwac krawedzie tak aby
miedzy kazda para wierzcholkow istniala tylko jedna unikatowa droga
Jezeli takich sciezek mamy kilka zostawiamy ta ktorej sumaryczna waga jest najwieksza
Zadanie sprowadza sie do znalezienia maximum spanning tree i odjecia jego wagi od
poczatkowej sumy wszystkich krawedzi - poniewaz w zadaniu mamy podac roznice
Dodatkowo nalezy oszczedzic jedna krawedz (najdrozsza usunieta) i odjac od roznicy
Wykorzystujemy funkcje przeksztalcajaca graf aby policzyc poczatkowa calkowita wage
a kruskala wykorzystujemy by policzyc wage drzewa
W glownej funkcji gdy mamy juz dostep do obu liczb i tablicy reprezentujacej drzewo
znajdujemy krawedz ktora ma sluzyc za wyjatek i wynikiem jest poczatkowa waga zmniejszona
o wage drzewa i 'wyjatkowej' krawedzi
'''
from egzP3btesty import runtests
from queue import PriorityQueue
def graph_change(G):
    edges = []
    graph_weight = 0
    for u in range(len(G)):
        for v, w in G[u]:
            edges.append((u, v, w))
            graph_weight += w
    return edges, graph_weight // 2

def kruskal_edges_modified(edges, V):
    edges.sort(key=lambda x: x[2], reverse = True)
    parent = list(range(V))

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        parent[find(u)] = find(v)

    mst = []
    mst_weight = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            mst_weight += w

    return mst, mst_weight

def lufthansa ( G ):
    ready1 = graph_change(G)
    edges = ready1[0]
    prev_result = ready1[1]
    V = len(G)

    ready2 = kruskal_edges_modified(edges, V)
    mst = ready2[0]
    result = ready2[1]

    max_exception = 0
    for a, b, c in edges:
        if c > max_exception and (a, b, c) not in mst and (b, a, c) not in mst:
            max_exception = c

    return prev_result - result - max_exception

runtests ( lufthansa, all_tests=True )