'''
Szymon Pytel
Naszym celem jest znalezc jak najkorzystniejszy ciag liczb z tablicy tak
aby suma ich maksymalnych czesci wspolnych byla jak najwieksza
Moim pomyslem jest stworzyc dwuwymiarowa tablice gdzie przechowujemy
najwieksze czesci wspolne przedzialow i na biezaco sprawdzamy maksymalna dotychczasowa sume
'''
from egzP5atesty import runtests

def inwestor ( T ):
    dp = [[0] * len(T) for _ in range(len(T))]
    roof = 0
    for row in range(len(T)):
        for col in range(row, len(T)):
            if row == col:
                dp[row][col] = T[row]
            else:
                dp[row][col] = min(dp[row][col-1], T[col])
            roof = max(roof, dp[row][col] * (col - row + 1))
    return roof

runtests ( inwestor, all_tests=False )