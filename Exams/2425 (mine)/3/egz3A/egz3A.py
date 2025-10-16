'''
Szymon Pytel
Moim pomyslem jest wykorzystac dwie petle, jedna przechodzac po kazdym elemencie tablicy H
a druga wracajac sie od niego na poczatek
Jesli trafimy na pare (i,j), gdzie H[i] > H[j], zmniejszamy k
Na biezaco monitorujemy wartosc k - jesli zejdzie do zera, stopujemy algorytm i zwracamy
indeks elementu do ktorego doszlismy
Zlozonosc rozwiazania to O(n^2)
'''
from egz3Atesty import runtests

def treecut( H, k ):
    n = len(H)
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            # idac w druga strone sprawdzamy jak liczba sie ma do poprzednich
            if H[i] > H[j]:
                k -= 1
        if k < 0:
            # odpuszczamy reszty porownan i konczymy algorytm jesli zachodzi warunek
            return j
    # jesli petla dotarla do konca logicznym jest ze odpowiedz to dlugosc tablicy
    return n

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( treecut, all_tests = True )
