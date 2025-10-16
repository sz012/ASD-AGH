'''
Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
wartość jest mniejsza od T [i].
Doprecyzowanie: Rozważmy tablicę [5,3,9,4]. W tej tablicy dwa pierwsze elementy mają
rangę 0 (nie poprzedza ich żaden mniejszy element), 3-ci element ma rangę 2 (przed nim w
tablicy znajdują się wartości 5 oraz 3), a ostatni ma rangę 1 (przed nim w tablicy jedynie 3 jest
mniejsze).
Proszę zaimplementować funkcję maxrank(T), która dla tablicy T o rozmiarze n elementów zwróci
maksymalną rangę pośród wszystkich elementów tablicy.
Przykład. Dla wejścia:
T = [5,3,9,4]
wywołanie maxrank(T) powinno zwrócić wartość 2 (odpowiadającą randze elementu na trzeciej
pozycji).
'''

'''
Szymon Pytel
Aby zrozumiec rozwiazanie, nalezy zrozumiec dzialanie merge sorta.
Gdy tablice dzielimy na dwie czesci, sklejamy je spowrotem w calosc w odpowiedniej kolejnosci, porownujac elementy.
Skupimy sie na elementach prawej tablicy. Jezeli cos z lewej jest od elementu mniejsze, trafia do posortowanej
tablicy, gdy jednoczesnie zwieksza sie i. Mozemy zatem iterator i uznac za ilosc elementow, ktore wystepowaly
przed dana liczba i byly od niej mniejsze. Wobec tego musimy wyciagnac pozycje tego elementu, do czego sluzy
nam tablica eT (zachowujaca w tuplach oryginalne pozycje) i do tej pozycji przypisac range zwiekszona o 1, w
tablicy ranks, ktora sluzy do przechowywania rang. Na koncu zwracamy wartosc maksymalna tablicy ranks.
'''
from kol1testy import runtests

def maxrank(T):
    ranks = [0 for x in range(len(T))]
    eT = [(T[k], k) for k in range(len(T))]

    def merge_sort(T):
        if len(T) <= 1:
            return T

        lT = T[:len(T) // 2]
        rT = T[len(T) // 2:]

        merge_sort(lT)
        merge_sort(rT)

        l = r = i = 0
        while l < len(lT) and r < len(rT):
            if lT[l] < rT[r]:
                T[i] = lT[l]
                l += 1
            else:
                T[i] = rT[r]
                r += 1
                (wartosc, indeks) = rT[r] #rownie dobrze - ranks[rT[r]] += i
                ranks[indeks] += i
            i += 1
        while l < len(lT):
            T[i] = lT[l]
            i += 1
            l += 1
        while r < len(rT):
            T[i] = rT[r]
            (wartosc, indeks) = rT[r] #rownie dobrze - ranks[rT[r]] += i
            ranks[indeks] += i
            r += 1
            i += 1
    return max(ranks)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = False )