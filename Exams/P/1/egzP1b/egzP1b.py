'''
Szymon Pytel
W zadaniu szukamy jak najkrotszej sciezki z punktu D do punktu L z tym ze
poruszajac sie w grafie G musimy przejsc przez dokladnie 3 wierzcholki
Wobec tego hipotetyczna krotsza droga przechodzaca przez 2 wierzcholki nie jest poprawnym rozwiazaniem
Moim pomyslem jest zastosowac tutaj algorytm dijkstry ktory na biezaco bedzie monitorowal
ilosc minietych wierzcholkow oraz porzucal drogi przekraczajace limit i odrzucal
rozwiazania nie spelniajace warunkow zadania
Nie wystarczy dodanie parametru mierzacego do kolejki
Nalezy stworzyc tablice dwuwymiarowa ktora dla kazdego dostepnego wierzcholka
zawrze koszt dotarcia po jednej dwoch oraz trzech atrakcjach
Tylko wtedy nie pominiemy zadnej poprawnej drogi
Rozwiazanie gwarantuje zlozonosc wzorcowa
'''
from egzP1btesty import runtests
from collections import defaultdict
import heapq

def dijkstra(graph, start, finish):

    # Tablica dwuwymiarowa zapamietuje wagi przejscia po minieciu 0, 1, 2 lub trzech atrakcji
    distances = defaultdict(lambda: [float('inf')] * 4)
    distances[start][0] = 0
    queue = [(0, start, 0)]

    while queue:
        curDist, curNode, curCounter = heapq.heappop(queue)
        if curDist > distances[curNode][curCounter]:
            continue

        for neighbor, weight in graph[curNode]:
            distance = curDist + weight

            # Lotnisko nie jest liczone jako atrakcja
            nextCounter = curCounter + 1 if neighbor != finish else curCounter

            # Jesli trafilismy na mete bierzemy pod uwage tylko wynik po minieciu trzech atrakcji
            if neighbor == finish and curCounter == 3 and distance < distances[neighbor][curCounter]:
                distances[neighbor][curCounter] = distance

            # Idziemy sciezka dalej jesli minelismy maksymalnie 3 atrakcje
            elif neighbor != finish and nextCounter <= 3 and distance < distances[neighbor][nextCounter]:
                distances[neighbor][nextCounter] = distance
                heapq.heappush(queue, (distance, neighbor, nextCounter))
    return min(distances[finish][3], float('inf'))

def turysta( G, D, L ):
    graph = defaultdict(list)
    for u, v, p in G:
        graph[u].append((v, p))
        graph[v].append((u, p))

    return dijkstra(graph, D, L)

runtests ( turysta )