'''
Szymon Pytel
Moim pomyslem jest wykorzystac zmodyfikowany knapsack problem (plecakowy), gdzie uwzgledniamy rowniez
mozliwosc wymiany punktow w "druga" strone z takim warunkiem, ze nie przekroczymy limitu zdrowia
(co ma sens poniewaz wyszlibysmy poza tablice)
Rzedy to kolejne plansze a kolumny to ilosc zdrowia jaka dysponujemy w danym momencie
Finalnie zwracamy wartosc maksymalna z ostatniego rzedu
Zlozonosc rozwiazania to O(nW)
'''
from egz3Btesty import runtests

def kom(X, Z, W):
    n = len(X)
    dp = [[-1] * (W + 1) for _ in range(n + 1)]
    dp[0][W] = 0
    for i in range(n):
        for z in range(W + 1):
            if dp[i][z] == -1:
                continue
            # idziemy dalej
            dp[i + 1][z] = max(dp[i + 1][z], dp[i][z])
            # wyscig - wymieniamy punkty zdrowia na punkty zwyciestwa
            if z - Z[i] >= 0:
                dp[i + 1][z - Z[i]] = max(dp[i + 1][z - Z[i]], dp[i][z] + X[i])
            # spa - wymieniamy punkty zwyciestwa na punkty zdrowia
            if dp[i][z] - X[i] > 0 and z + Z[i] <= W:
                dp[i + 1][z + Z[i]] = max(dp[i + 1][z + Z[i]], dp[i][z] - X[i])
    return max(dp[n])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kom, all_tests = True )
