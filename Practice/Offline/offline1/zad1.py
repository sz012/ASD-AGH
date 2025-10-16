'''
Mówimy, że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne,
gdyby jeden z nich zapisać od tyłu. Na przykład napisy “kot” oraz “tok” są sobie równoważne,
podobnie jak napisy “pies” i “pies”. Dana jest tablica T zawierająca n napisów o łącznej długości
N (każdy napis zawiera co najmniej jeden znak, więc N ≥ n; każdy napis składa się wyłącznie z
małych liter alfabetu łacińskiego). Siłą napisu T [i] jest liczba indeksów j takich, że napisy T [i]
oraz T [j] są sobie równoważne. Napis T [i] jest najsilniejszy, jeśli żaden inny napis nie ma większej
siły.
Proszę zaimplementować funkcję g(T), która zwraca siłę najsilniejszego napisu z tablicy T . Na
przykład dla wejścia:
# 0 1 2 3 4 5 6
T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
wywołanie g(T) powinno zwrócić 3. Algorytm powinien być możliwie jak najszybszy. Proszę podać
złożoność czasową i pamięciową zaproponowanego algorytmu.
'''
'''
Szymon Pytel
Poniewaz zalezy nam na jak najmniejszej zlozonosci, nie odpowiada nam rozwiazanie ktore od razu przychodzi na mysl.
Nalezy najpierw posortowac tablice, aby napisy byly obok siebie, wtedy algorytm bedzie prostszy dla komputera
oraz znajdziemy najsilniejszy napis po kolei iterujac po tablicy, albo dodajac 1 do licznika, albo porownujac
moc napisu do mocy maksymalnej.
Sortowanie przeprowadze metoda merge sort.
'''
from zad1testy import runtests

def merge_sort(T):
    if len(T) > 1:
        lT = T[:len(T)//2]
        rT = T[len(T)//2:]

        merge_sort(lT)
        merge_sort(rT)
        l = 0
        r = 0
        i = 0
        while l < len(lT) and r < len(rT):
            if lT[l] < rT[r]:
                T[i] = lT[l]
                l += 1
            else:
                T[i] = rT[r]
                r += 1
            i += 1
        while l < len(lT):
            T[i] = lT[l]
            i += 1
            l += 1
        while r < len(rT):
            T[i] = rT[r]
            i += 1
            r += 1
    return T

def strong_string(T):
    newT = [min(napis, napis[::-1]) for napis in T]
    merge_sort(newT)

    counter = 0
    max_counter = 0
    for k in range(1, len(newT)):
        if newT[k] == newT[k-1]:
            counter += 1
        else:
            max_counter = max(max_counter, counter)
            counter = 1
    return max_counter


# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( strong_string, all_tests=True )
