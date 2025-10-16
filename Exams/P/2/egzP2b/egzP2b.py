'''
Szymon Pytel
Kod ma za zadanie zwrocic maksymalna mozliwa ilosc wiadomosci
ktorych sufiksy mamy podane w tablicy Q
Tablica D to lista binarnych slow do ktorych pasowac beda
elementy z raportu Q
Algorytm ma zrocic logarytm dziesietny z finalnego wyniku
'''
from egzP2btesty import runtests
from math import log10
import bisect

def kryptograf(D, Q):
    for i in range(len(D)):  # nm
        D[i] = D[i][::-1]

    for i in range(len(Q)):  # qm
        Q[i] = Q[i][::-1]

    D.sort()  # nmlog(nm)

    output = 1
    # q * środek
    for i in Q:
        # m*log(n)
        lo = bisect.bisect_left(D, i)
        hi = bisect.bisect_right(D, i + "2")
        output *= hi - lo
    return log10(output)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=3)