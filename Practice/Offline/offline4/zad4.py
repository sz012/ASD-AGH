'''
Układ planetarny Algon składa się z n planet o numerach od 0 do n− 1. Niestety własności fizyczne
układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na szczęście
mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpośrednich
przelotów. Każdy element listy E to trójka postaci (u, v, t), gdzie u i v to numery planet (można
założyć, że u < v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co z v do u).
Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują się w okolicy
osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni umożliwiające
przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym.
Zadanie polega na zaimplementowaniu funkcji:
def spacetravel( n, E, S, a, b )
która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych
bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie
istnieje, to funkcja powinna zwrócić None.
Rozważmy następujące dane:
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7
21
4
6
1
1
5
wywołanie spacetravel(n, E, S, a, b) powinno zwrócić liczbę 13. Odwiedzamy po kolei planety
1, 3, 2, 4, 6 i kończymy na planecie 5 (z planety 2 do 3 dostajemy się przez zagięcie czasoprzestrzeni).
Gdyby a =1 a b=2 to wynikiem byłby czas przelotu 1.
'''
'''
Szymon Pytel
'''
from zad4testy import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0

    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        cur_distance, v = PQ.get()

        if cur_distance > distance[v]:
            continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                PQ.put((dist, v_son))

    return distance[e]


def spacetravel(n, E, S, a, b):

    G = [[] for _ in range(n+1)]

    #zamiana z postaci (u,v,w) na adjency list
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    for i in S:
        G[n].append((i,0))
        G[i].append((n,0))

    time = dijkstra(G,a,b)

    return time if time<float('inf') else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
