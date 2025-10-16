#O(n)
#przydatny w zadaniach gdzie nalezy znalezc k-ty najwiekszy/najmniejszy element
#quickselect to praktyczna implementacja algorytmu quicksort, ale zamiast sortowac cala tablice,
#zwraca k-ty najwiekszy element

def partition(T, l, r):
    i = l
    j = r - 1
    pivot = T[r]

    while i < r and j > r:
        while i < r and T[i] <= pivot:
            i += 1
        while j > l and T[j] >= pivot:
            j -= 1
        if i < j:
            T[i], T[j] = T[j], T[i]
    if T[i] > pivot:
        T[i], T[r] = T[r], T[i]
    return i

def quickselect(T, l, r, k): #k oznacza k-ty najwiekszy element
    if r >= l:
        partition_position = partition(T, l, r)
        if partition_position == k:
            return T[k]
        elif k < partition_position:
            return quickselect(T, l, partition_position - 1, k)
        else:
            return quickselect(T, partition_position + 1, r, k)




