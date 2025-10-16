'''
Szymon Pytel
Zadanie z programowania dynamicznego gdzie musimy znalezc kombinacje par elementow w tablicy o mozliwe jak
najmniejszej sumie roznic miedzy parami
Dodatkowa trudnosc jest taka, ze 'kable' ktore lacza liczby sie nie moga krzyzowac co daje nam pewnosc
ze w kodzie na pewno wystapia pary sasiadow
'''
from egz2atesty import runtests

def wired(T):
  n = len(T)
  dp = [[float('inf')] * n for _ in range(n)]

  # Każdy pusty lub jednoelementowy przedział ma koszt 0
  for i in range(n):
    dp[i][i] = 0
    if i + 1 < n:
      dp[i + 1][i] = 0  # dla przypadków gdzie j < i

  # Rozpatrujemy przedziały o rosnącej długości
  for length in range(2, n + 1, 2):  # tylko parzyste długości
    for i in range(n - length + 1):
      j = i + length - 1
      for k in range(i + 1, j + 1, 2):  # próbujemy połączyć i z k
        left = dp[i + 1][k - 1] if k - 1 >= i + 1 else 0
        right = dp[k + 1][j] if k + 1 <= j else 0
        cost = 1 + abs(T[i] - T[k])
        dp[i][j] = min(dp[i][j], left + right + cost)

  return dp[0][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )
