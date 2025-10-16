'''
Szymon Pytel
Trwa wyscig autonomicznych robotow ktore przemierzaja punkty kontrolne w grafie
Musza je odwiedzic w kolejnosci zadanej w tablicy P
Algorytm ma podac koszt przejscia sciezki w grafie podanym przez G
Moim pomyslem jest zastosowac dijkstre w petli zapisujac wierzcholek do ktorego ostatnio dotarlismy
'''
from egzP8btesty import runtests
import heapq
from collections import defaultdict

def graph_change(graph):
    new_graph = defaultdict(list)
    for i in range(len(graph)):
        new_graph[i].append(graph[i])
        new_graph[i] = new_graph[i][0]
    return new_graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        currentDistance, currentNode = heapq.heappop(queue)
        if currentDistance > distances[currentNode]:
            continue
        for neighbor, weight in graph[currentNode]:
            distance = currentDistance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def robot( G, P ):
    graph = graph_change(G)
    res = 0
    for m in range(1, len(P)):
        arr = dijkstra(graph, P[m-1])
        res += arr[P[m]]
    return res
    
runtests(robot, all_tests = True)
