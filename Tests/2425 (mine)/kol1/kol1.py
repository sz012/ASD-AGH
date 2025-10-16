'''
Szymon Pytel
Moim pomyslem jest poczatkowo posortowanie tablicy lokalizacji palików metodą
merge sort, a nastepnie znalezienie wszystkich roznic między nimi w posortowanej tablicy,
by w końcu wypisać w ilu miejscach może przejechać kombajn
'''
from kol1testy import runtests

def ogrodzenie(M, D, T):
    def merge_sort(T):
        if len(T) > 1:
            lT = T[:len(T) // 2]
            rT = T[len(T) // 2:]

            merge_sort(lT)
            merge_sort(rT)

            i = 0
            j = 0
            k = 0
            while i < len(lT) and j < len(rT):
                if lT[i] < rT[j]:
                    T[k] = lT[i]
                    i += 1
                else:
                    T[k] = rT[j]
                    j += 1
                k += 1
            while i < len(lT):
                T[k] = lT[i]
                i += 1
                k += 1
            while j < len(rT):
                T[k] = rT[j]
                j += 1
                k += 1

    merge_sort(T)
    counter = 0
    for k in range(1, len(T)):
        if T[k] - T[k - 1] >= D:
            counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ogrodzenie, all_tests=True)
