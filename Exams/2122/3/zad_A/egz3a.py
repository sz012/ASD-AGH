'''
Szymon Pytel
W tablicy T mamy podana dlugosc autostrady a tablicy I przedzialy autostrady na ktorych z
kazdym kolejnym dniem podnosi sie poziom sniegu
Numery dni reprezentuja indeksy tablicy przedzialow
Zadaniem algorytmu jest znalezc punkt na autostradzie gdzie po uplywie ostatniego dnia
poziom sniegu bedzie najwyzszy - zakladamy ze snieg nie topnieje
Problematyka zadania sproawdza sie do algorytmu sweep line gdzie szukamy momentu
w ktorym w restauracji znajduje sie najwiecej klientow, gdy podano nam tablice
zawierajaca przedzialy czasowe ich obecnosci
Nalezy stworzyc nowa tablice ktora okresli kiedy ktos przychodzi a kiedy odchodzi a nastepnie ja posortowac
Pozostaje tylko przejsc po niej iteratorem i wyznaczyc maksymalna liczbe
Rozwiazanie gwarantuje zlozonosc wzorcowa O(nlogn)
'''
from egz3atesty import runtests

def merge_sort_sl(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        merge_sort_sl(leftArr)
        merge_sort_sl(rightArr)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i][0] < rightArr[j][0]:
                arr[k] = leftArr[i]
                i += 1
            elif leftArr[i][0] == rightArr[j][0]:
                if leftArr[i][1] > rightArr[j][1]:
                    arr[k] = leftArr[i]
                    i += 1
                else:
                    arr[k] = rightArr[j]
                    j += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        while i < len(leftArr):
            arr[k] = leftArr[i]
            k += 1
            i += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            k += 1
            j += 1

def snow( T, I ):
    events = []
    for e in range(len(I)):
        events.append((I[e][0], 1))
        events.append((I[e][1], -1))
    merge_sort_sl(events)

    max_ctr = 0
    ctr = 0
    for time, decision in events:
        ctr += decision
        max_ctr = max(max_ctr, ctr)

    return max_ctr

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
