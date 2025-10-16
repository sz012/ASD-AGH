'''
Szymon Pytel
W liscie X podane mamy indeksy biurowcow, a w Y parkingow
Program ma na celu znalezc minimalna sume odleglosci miedzy biurowcami a parkingami
biorac pod uwage fakt ze parking biurowca 'i' musi byc przed parkingiem biurowca 'i+1'
Kazdy biurowiec ma miec swoj wlasny jeden parking. Ilosc parkingow jest wieksza niz biurowcow
Moja metoda rozwiazania to programowanie dynamiczne, wyzej zakomentowana jest wersja zachlanna
z nierozwiazanymi dotad bledami
W tablicy dwywymiarowej, gdzie rzedy to biurowce a kolumny to parkingi, na biezaco uzupelniamy
komorki, gdzie komorki [n][m] znaczy 'koszt polaczenia biurowca n z parkingiem m' + 'minimalny koszt polaczen do tej pory'
Rozwiazaniem jest minimalna liczba jaka wyjdzie w ostatnim wierszu, poniewaz tabela wszystko sumuje i progresywnie dochodzimy
do rozwiazania, gdzie w wierszu o ostatnim indeksie w danej komorce mowimy ile nas bedzie kosztowac polaczenie
ostatniego biurowca z danym parkingiem, zakladajac ze wszystkie poprzednie polaczymy najlepiej jak sie da
'''
from egz2btesty import runtests
'''
def parking(X,Y):
  sum = i = j = 0
  while i < len(X):
    min_odl = float('inf')
    while j < (len(Y) - (len(X) - i - 1)):
      if abs(X[i] - Y[j]) < min_odl:
        min_odl = abs(X[i] - Y[j])
        min_odl_j = j
      j += 1
    sum += min_odl
    j = min_odl_j + 1
    i += 1
  return sum
'''

def parking(X, Y):
  m, n = len(Y), len(X)
  dp = [[float('inf')] * m for _ in range(n)]

  for j in range(m - n + 1):
    dp[0][j] = abs(X[0] - Y[j])

  for i in range(1, n):
    min_poprzedni = float('inf')
    for j in range(i, m):
      min_poprzedni = min(min_poprzedni, dp[i - 1][j - 1])
      dp[i][j] = abs(X[i] - Y[j]) + min_poprzedni

  return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = False )
