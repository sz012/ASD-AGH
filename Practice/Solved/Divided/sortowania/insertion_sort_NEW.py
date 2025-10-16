'''
O(n^2)
Algorytm nalezacy do prostych, bardzo podobny do selection sorta
Dziala on natomiast w druga strone
Idziemy tutaj po kazdym elemencie oraz znajdujemy jego miejsce
cofajac go do tylu w tablicy
'''

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

arr = [5, 3, 3, 0, 1, 9, 8, 2]
print(insertion_sort(arr))