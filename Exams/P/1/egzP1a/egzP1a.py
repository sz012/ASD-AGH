'''
Szymon Pytel
Zadanie to klasyczny problem string segmentation z dodatkowymi trudnosciami
Mamy do dyspozycji alfabet morsa w tablicy M oraz wybrane z niego litery w tablicy D
Naszym zadaniem jest przedstawic wiadomosc W przy uzyciu dostepnych liter
Priorytetem przy wyborze liter jest ich ilosc
Wiadomosc ma zostac przedstawiona przy uzyciu jak najmniejszej ilosci liter
Wykorzystuje tutaj metode programowania dynamicznego gdzie zgodnie z indeksami
zapisuje minimalna ilosc liter potrzebnych do reprezentacji napisu do danego indeksu
Aby przyspieszyc dzialanie algorytmu i ograniczyc niepotrzebne obliczenia z tablicy
dostepnych liter tworze zbior oraz zbior ich dlugosci w reprezentacji morsa
Rozwiazanie gwarantuje zlozonosc wzorcowa
'''

from egzP1atesty import runtests

def titanic(W, M, D):
    new_w = ''.join([M[n][1] for m in W for n in range(len(M)) if M[n][0] == m])
    av_let = set(M[id][1] for id in D)
    lens = set(len(l) for l in av_let)
    dp = [float('inf')] * (len(new_w) + 1)
    dp[0] = 0

    #new_w - napis po ktorym bedziemy sie poruszac w programowaniu dynamicznym
    #av_let - tablica dostepnych znakow na ktore podzielimy napis
    #dp[i] - minimalna ilosc czesci na ktore podzielony zostal napis new_w[:i]

    for i in range(1, len(new_w) + 1):
        for l in lens:
            if i - l >= 0 and new_w[i-l:i] in av_let:
                dp[i] = min(dp[i], dp[i-l] + 1)
    return dp[len(new_w)]

runtests ( titanic, recursion=False )