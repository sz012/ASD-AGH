'''
Szymon Pytel
Na tablicy znajduja sie katapulty i procesory, katapulty strzelaja do procesorow
Katapulta moze strzelac tylko do przodu i ma ograniczony zasieg
P - pozycje procesorow
K - pozycje katapult
R - zasiegi katapult
Nie wszystkie katapulty musza strzelac
Zadaniem programu jest podac maksymalna liczbe procesorow do ktorych moga strzelac katapulty
Moj pomysl to algorytm dynamiczny z tablica dwuwymiarowa dp
dp[i][j] = max liczba trafionych procesorów używając pierwszych i katapult i pierwszych j procesorów
'''

from egz1Atesty import runtests
def battle(P, K, R):
    n = len(P)
    m = len(K)

    P.sort()
    katapulty = sorted(zip(K, R))
    print(katapulty)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        cur_pos, cur_range = katapulty[i - 1]

        for j in range(1, n + 1):

            dp[i][j] = max(dp[i][j], dp[i - 1][j])

            if P[j - 1] > cur_pos and P[j - 1] <= cur_pos + cur_range:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

            else:

                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[m][n]

'''
porzucony pomysl
def battle_nevermin(P, K, R):
    n = len(P)
    m = len(K)

    P.sort()
    katapulty = sorted(zip(K, R))
    print(katapulty)

    dp = [[0] * (n) for _ in range(m)]
    for i in range(m):
        cur_pos, cur_range = katapulty[i]
        for j in range(n):
            if P[j] > cur_pos and P[j] <= cur_pos + cur_range:
                dp[i][j] = 1
    for r in range(m-1, 0, -1):
        for c in range(n-2, 0, -1):
            if dp[r-1][c] == 0:
                dp[r-1][c] = dp[r][c] + 1
            else:
                dp[r-1][c+1] = dp[r][c] + 1
    return max(dp[0])
'''

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=False)
