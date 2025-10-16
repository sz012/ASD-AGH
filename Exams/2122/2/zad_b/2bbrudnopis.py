'''
Szymon Pytel

W tablicy C sa wypisane komnaty jaskini zawierajace kredyty w skrzyni oraz po trzy pary drzwi
prowadzace do kolejnych komnat lub zupelnie zablokowane
Czarodziej musi sie przedostac od pierwszej do ostatniej komnaty zabierajac ze soba mozliwie
najwiecej sztabek zlota ktore zbiera w skrzyniach oraz wydaje na przejscia przez drzwi
ktorych koszta sa podane obok numerow komnat do ktorych prowadza

Chcialbym stworzyc graf skierowany ktory bedzie reprezentowal nasza jaskinie
Krawedzie to beda oczywiscie przejscia miedzy komnatami, a ich wagi
to roznice miedzy kredytami w skrzynce docelowego wierzcholka a kosztem przejscia przez drzwi do niego
W takiej sytuacji pozostaje nam zastosowac algorytm bellmana-forda z uwagi na to ze niektore wagi beda ujemne
'''

from egz2btesty import runtests


# C: [skrzynia, [koszt, komnata], [koszt, komnata], [koszt, komnata]]

def bellman_ford_modified(graph, start):
    V = len(graph)
    distances = [-float('inf')] * V

    '''
    for k in range(len(graph)):
        if graph[k][0] > 10: graph[k][0] = 10
    distances[start] = graph[start][0]
    '''

    for i in range(V - 1):
        updated = False
        for u in range(V):
            for w, v in graph[u][1:]:
                if v == -1: continue
                '''
                if distances[u] - w + graph[v][0] > distances[v]:
                    distances[v] = distances[u] - w + graph[v][0]
                    updated = True
                '''

        if not updated:
            break

    '''
    for u in range(V):
        for w, v in graph[u][1:]:
            if v == -1: continue
            if distances[u] - w + graph[v][0] > distances[v]:
                print('Cykl o ujemnej wadze')
                return None
    '''
    return distances


def magic(C):
    res = bellman_ford_modified(C, 0)
    if res[-1] == -float('inf'): return -1
    return res[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)