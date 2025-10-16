'''
Szymon Pytel
Mamy graf dwudzielny z taka sama iloscia wierzcholkow po obu stronach
W tablicy T podane sa propozycje mostow miedzy nimi i zadaniem programu
jest obliczyc ile najwiecej mozemy ich zbudowac tak aby zadne mosty sie nie przecinaly
Zakladamy ze wierzcholki sa ustawione po kolei w dwoch rzedach
Moim pomyslem jest wykorzystac tablice dwuwymiarowa i idac komorka po komorce
zapisywac maksymalna mozliwa ilosc polaczen
'''
from egzP4atesty import runtests

def mosty ( T ):
    furthest = 0
    for i in range(len(T)):
        furthest = max(furthest, T[i][0], T[i][1])

    dp = [[0] * (furthest + 1) for _ in range(furthest + 1)]
    for j in range(len(T)):
        dp[T[j][0]][T[j][1]] = 1

    # Jesli mamy most od wierzcholka 0 to nie mozemy sie odnosic do komorek powyzej
    for k in range(1, len(dp)):
        dp[0][k] = max(dp[0][k], dp[0][k-1])

    for row in range(1, len(dp)):
        if dp[row-1][0] == 1:
            dp[row][0] = 1

        for col in range(1, len(dp)):
            if dp[row][col] == 1:
                dp[row][col] += dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])

    return dp[-1][-1]

runtests ( mosty, all_tests=True )