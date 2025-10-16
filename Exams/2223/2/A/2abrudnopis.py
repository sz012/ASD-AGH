from egz2atesty import runtests

def merge_sort(arr, place):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        merge_sort(leftArr, place)
        merge_sort(rightArr, place)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i][place] < rightArr[j][place]:
                arr[k] = leftArr[i]
                i += 1
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


def dominance_counter(P, idx, length):
    ctr = 0
    for j in range(0, idx - length):
        if P[j][1] < P[idx][1]:
            ctr += 1
    return ctr

def dominance(P):
    max_ctr = 0

    # Sortowanie po x-ach
    merge_sort(P, 0)

    start_idx = 0
    for i in range(len(P)):

        # Sortowanie po y-ach
        if P[i][0] != P[start_idx][0] or i == len(P) - 1:
            subarr = P[start_idx:i]
            merge_sort(subarr, 1)
            P[start_idx:i] = subarr

            # Gdy mamy posortowany podciag sensownym jest sprawdzic tylko jego ostatni element
            # Przykladowo (1,1) (1,2) *(1,3)* / (8,5) *(8,20)* / *(100,100)*
            max_ctr = max(max_ctr, dominance_counter(P, i, len(subarr)))

            start_idx = i
    return max_ctr

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = False )