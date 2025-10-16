'''
Dana jest tablica T zawierająca liczby naturalne. Proszę napisać funkcję count inversions(T),
która dla tablicy zwraca liczbę inwersji w tablicy.
Na przykład dla wejścia:
T = [1,20,6,4,5]
wywołanie count inversion(T) powinno zwrócić 5. Algorytm powinien być możliwie jak najszyb-
szy. Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.
'''
'''
Szymon Pytel
Liczba inwersji w tablicy to liczba takich par indeksow (i, j), gdzie i < j oraz T[i] > T[j].
Innymi slowy to ilosc liczb przed danym elementem, ktore sa od niego wieksze.
Zauwazam, ze metoda sortowania merge sort pozwala w trakcie jej stosowania zliczyc ilosc
par takich indeksow.
Rozwiazanie zadania to spersonalizowany algorytm merge sort.
'''
from zad2testy import runtests

def count_inversions(A):
    if len(A) <= 1:
        return 0
    lA = A[:len(A)//2]
    rA = A[len(A)//2:]
    count_inversions_l = count_inversions(lA)
    count_inversions_r = count_inversions(rA)
    inversion_counter_merge = 0
    l = 0
    r = 0
    i = 0
    while l < len(lA) and r < len(rA):
        if lA[l] < rA[r]:
            A[i] = lA[l]
            l += 1
        else:
            A[i] = rA[r]
            r += 1
            inversion_counter_merge += len(lA) - l # Wszystkie pozostałe elementy w lA są większe od rA[r]
            # ponieważ lA jest posortowane
        i += 1
    while l < len(lA):
        A[i] = lA[l]
        l += 1
        i += 1
    while r < len(rA):
        A[i] = rA[r]
        r += 1
        i += 1

    return inversion_counter_merge + count_inversions_l + count_inversions_r


# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
