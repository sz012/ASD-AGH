#O(nlogn)
def quicksort(T, l, r):
    if l < r:
        partition_position = partition(T, l, r) #wyznaczenie miejsca pivota
        quicksort(T, partition_position + 1, r) #rekurencja prawo
        quicksort(T, l, partition_position - 1) #rekurencja lewo

def partition(T, l, r):
    i = l
    j = r - 1
    pivot = T[r] #pivot zawsze zaczyna od ostatniego miejsca w tablicy
    #uwaga! pivot to wartosc, a nie indeks

    while i < j:
        while i < r and T[i] < pivot:
            i += 1 #i porusza się w prawo i zatrzymuje gdy znajdzie wart. >= pivot
        while j > l and T[j] >= pivot:
            j -= 1 #j porusza się w lewo i zatrzymuje gdy znajdzie wart. < pivot
        if i < j:
            T[i], T[j] = T[j], T[i] #jeśli i oraz j nie zdążą się minąć, zamieniamy je miejscami

    if T[i] > pivot:
        T[i], T[r] = T[r], T[i] #jeśli i oraz j się miną, wartość i zamieniamy z pivotem

    return i #ponieważ tu zwracamy tylko położenie pivota dla funkcji quicksort
#test
T = [5, 3, 0, 0, 2, 8, 7, 1, 4, 2]
quicksort(T, 0, len(T) - 1)
print(T)
