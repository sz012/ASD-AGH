'''
Szymon Pytel
Programowanie dynamiczne - szukamy najtanszej drogi
z poczatku na koniec tablicy
Przebycie z jednej planety na druga kosztuje okreslona ilosc benzyny,
ktora mozemy tankowac na kazdej planecie, przy czym ceny sie roznia
Do tego jest opcja teleportacji miedzy planetami
Najefektywniejszym rozwiazaniem jest stworzenie tablicy dwuwymiarowej
gdzie wiersze to planety a kolumny to ilosc benzyny jaka hipotetycznie bysmy
mogli dysponowac
'''
from egz1btesty import runtests

def planets( D, C, T, E ):
    costs = [[float('inf') for _ in range(E + 1)] for _ in range(len(D))]
    costs[0][0] = 0

    # [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] planeta 0
    # [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] planeta 1
    # [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] plaenta 2
    # [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] planeta 3

    for i in range(len(D) - 1):
        for j in range(1, E + 1):
            costs[i][j] = min(costs[i][j], costs[i][j - 1] + C[i])
        if T[i][0] > i:
            costs[T[i][0]][0] = min(costs[T[i][0]][0], costs[i][0] + T[i][1])
        dist = D[i + 1] - D[i]
        for k in range(dist, E + 1):
            costs[i + 1][k - dist] = min(costs[i + 1][k - dist], costs[i][k])
    return costs[len(D) - 1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = False )
