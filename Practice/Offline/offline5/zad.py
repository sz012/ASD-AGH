'''
Dobrycerz (czyli rycerz, który zawsze uprzejmie mówi “dzień dobry”) chce się przedostać z zamku s
do zamku t. Mapa zamków dana jest w postaci grafu nieskierowanego G, gdzie każda krawędź ma wa-
gę oznaczającą ile godzin potrzeba, żeby ją przebyć. Wagi to liczby naturalne ze zbioru {1, 2, . . . , 8}.
Po najdalej 16 godzinach podróży Dobrycerz musi nocować w zamku. Warunki uprzejmości wy-
magają, żeby spędził w takim zamku 8 godzin (przejazd przez zamki, w których nie nocuje nie
kosztuje dodatkowego czasu; szybko mówi “dzień dobry” strażnikom i jedzie dalej). Mapa z której
korzysta Dobrycerz ma to do siebie, że liczba dróg jest proporcjonalna do liczby zamków. Czyli jeśli
zamków jest n, to wiadomo, że dróg jest O(n).
Zadanie polega na implementacji funkcji:
goodknight( G, s, t )
która na wejściu otrzymuje graf opisujący mapę zamków, reprezentowany w postaci macierzy są-
siedztwa (czyli G[i][j] to liczba godzin, konieczna do przejechania bezpośrednio z zamku i do
zamku j; w przypadku braku drogi G[i][j]=−1), zamek startowy s oraz zamek docelowy t, i
zwraca minimalny czas (wyrażony w godzinach) potrzebny na przejazd z s do t (Dobrycerz nigdy
nie musi nocować ani w zamku s ani w zamku t). Można założyć, że zawsze istnieje trasa z zamku
s do t.
Przykład. Dla wejścia:
# 0 1 2 3 4 5
G = [ [ -1, 3, 8,-1,-1,-1 ], # 0
[ 3,-1, 3, 6,-1,-1 ], # 1
[ 8, 3,-1,-1, 5,-1 ], # 2
[ -1, 6,-1,-1, 7, 8 ], # 3
[ -1,-1, 5, 7,-1, 8 ], # 4
[ -1,-1,-1, 8, 8,-1 ]] # 5
1 3 5
6 8
3 7
3 8
s = 0
t = 5
wynikiem jest 25. Dobrycerz pokonuje następującą trasę:
1. Jedzie z zamku 0 do zamku 1 (3 godziny).
2. Jedzie z zamku 1 do zamku 3 (6 godzin).
3. Nocuje w zamku 3 (8 godzin).
4. Jedzie z zamku 3 do zamku 5 (8 godzin)
'''
'''
Szymon Pytel
'''
from zadtesty import runtests
from queue import PriorityQueue

def dijkstra_goodknight(G, s, t):
    n = len(G)

    # distance[v][h] = najmniejszy czas dotarcia do v z h godzinami marszu bez snu
    distance = [ [float("inf")] * 9 for _ in range(n) ]  # bo max 8h

    distance[s][0] = 0
    Q = PriorityQueue()
    Q.put((0, s, 0))  # (koszt całkowity, wierzchołek, godziny bez snu)

    while not Q.empty():
        cost, v, hours = Q.get()

        if cost > distance[v][hours]:
            continue

        for u in range(n):
            weight = G[v][u]
            if weight == -1:
                continue  # brak krawędzi

            # OPCJA 1: Idziemy dalej bez noclegu
            if hours + weight <= 8:
                if cost + weight < distance[u][hours + weight]:
                    distance[u][hours + weight] = cost + weight
                    Q.put((cost + weight, u, hours + weight))

            # OPCJA 2: Nocujemy (o ile u != s i u != t)
            if u != s and u != t:
                if cost + weight + 8 < distance[u][0]:
                    distance[u][0] = cost + weight + 8
                    Q.put((cost + weight + 8, u, 0))

    return min(distance[t])  # minimalny koszt dojścia do t z dowolną liczbą godzin bez snu

def goodknight(G, s, t):
    return dijkstra_goodknight(G, s, t)



runtests(goodknight, all_tests=True)
