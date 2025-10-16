 #DO KOREKTY
'''
O(n)
Caly kod opiera sie na quicksorcie i mozna powiedziec
ze to lekko spersonalizowana forma tego algorytmu
Nie sluzy on do samego sortowania, a znalezienia
k-tego najwiekszego elementu
Powolujac sie na dzialanie quicksorta bez konsekwencji mozemy
pominac kilka krokow koncentrujac sie na danych czesciach tablicy
'''
def partition(arr, lIdx, rIdx):
    pivot = arr[rIdx]
    i = lIdx
    for j in range(lIdx, rIdx):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[rIdx] = arr[rIdx], arr[i]

    return i

def quickselect(arr, lIdx, rIdx, k):
    if lIdx <= rIdx:
        partition_position = partition(arr, lIdx, rIdx)
        if partition_position == k:
            return arr[k]
        elif k < partition_position:
            return quickselect(arr, lIdx, partition_position - 1, k)
        else:
            return quickselect(arr, partition_position + 1, rIdx, k)

arr = [2, 4, 0, 1, 5]
print(quickselect(arr, 0, len(arr) - 1, 1))