'''
O(nlogn)
Sortowanie szybkie
Algorytm zlozonosciowo na rowni z merge sortem
Charakteryzuje sie pivotem, ktory wyznacza w ktorym miejscu
dzielimy tablice na czesci, sortujac je dalej rekurencyjnie dwoma iteratorami
'''

def partition(arr, lIdx, rIdx):
    i, j = lIdx, rIdx - 1
    pivot = arr[rIdx]

    while i < j:
        while i < rIdx and arr[i] < pivot:
            i += 1
        while j > lIdx and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[rIdx] = arr[rIdx], arr[i]

    return i


def quicksort(arr, lIdx, rIdx):
    if lIdx < rIdx:
        partition_position = partition(arr, lIdx, rIdx)
        quicksort(arr, partition_position + 1, rIdx)
        quicksort(arr, lIdx, partition_position - 1)

arr = [2, 4, 1, 0, 7, 5, 3, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)
