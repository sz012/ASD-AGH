'''
Dana jest n-elementowa tablica liczb naturalnych T oraz dodatnie liczby naturalne k i p, gdzie
k ≤ p ≤ n. Niech zi będzie k-tą największą spośród elementów: T[i], T[i+1], ..., T[i+p-1]. Innymi
słowy, zi to k-ty największy element w T w przedziale indeksów od i do i + p− 1 włącznie.
Doprecyzowanie: Rozważmy tablicę [17,25,25,30]. W tej tablicy 1-wszy największy element
to 30, 2-gi największy element to 25, 3-ci największy element to także 25 (drugie wystąpienie), a
4-ty największy element to 17.
Proszę zaimplementować funkcję ksum(T, k, p), która dla tablicy T (o rozmiarze n elementów) i
dodatnich liczb naturalnych k i p (k ≤ p ≤ n) wylicza i zwraca wartość sumy:
z0 + z1 + z2 + . . . + zn−p
'''
'''
Szymon Pytel
'''
from kol1testy import runtests

def partition(T, l, r):
    i = l
    j = r - 1
    pivot = T[r]

    while i < j:
        while i < r and T[i] <= pivot:
            i += 1
        while j > l and T[j] >= pivot:
            j -= 1
        if i < j:
            T[i], T[j] = T[j], T[i]
    if T[i] > pivot:
        T[i], T[r] = T[r], T[i]
    return i

def quickselect(T, l, r, k):
    if l <= r:
        partition_position = partition(T, l, r)
        if k == partition_position:
            return T[k]
        elif k < partition_position:
            return quickselect(T, l, partition_position - 1, k)
        else:
            return quickselect(T, partition_position + 1, r, k)


def ksum(T, k, p):
    sum = 0
    for n in range(len(T) - p + 1):
        newT = T[n:n + p]
        sum += quickselect(T, 0, len(newT) - 1, k - 1)
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False )