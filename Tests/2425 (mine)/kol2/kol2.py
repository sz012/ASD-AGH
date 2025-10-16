'''
Szymon Pytel
Moim pomyslem jest poczatkowa zmiana reprezentacji grafu aby uproscic algorytm dijkstry
i wykonywanie dijkstry w petli, za kazdym razem dodajac kurorty do tablicy ignorowanych wierzcholkow
Petla przy okazji zawsze znajduje najmniej kosztowny kurort, poniewaz wedlug tresci zadania
tym sie sugeruje kolejnosc odwiedzania
'''
from kol2testy import runtests
import heapq
from collections import defaultdict

def make_graph(graph):
    new_graph = defaultdict(list)
    for u, v, c in graph:
        new_graph[u].append((v, c))
        new_graph[v].append((u, c))
    return new_graph

def dijkstra_modified(graph, start, ignored):
    distances = [float('inf')] * len(graph)
    distances[start] = 0

    queue = [(0, start)]
    while queue:
        curDist, curNode = heapq.heappop(queue)
        if curDist > distances[curNode]:
            continue
        if curNode in ignored:
            continue
        for neighbor, weight in graph[curNode]:
            distance = curDist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def lets_roll(start_city, flights, resorts):
    sum = 0
    ignored = []
    new_flights = make_graph(flights)

    while len(resorts) > len(ignored):
        distances = dijkstra_modified(new_flights, start_city, ignored)
        min_distance = float('inf')
        for resort in resorts:
            if min_distance > distances[resort] and resort not in ignored:
                min_distance = distances[resort]
                chosen_resort = resort
        if min_distance == float('inf'): return sum
        sum += 2 * min_distance
        ignored.append(chosen_resort)
    return sum

runtests(lets_roll, all_tests = False)

