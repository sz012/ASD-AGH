'''
O(n^2)
Najbardziej podstawowy/klasyczny algorytm sortowania
z niezbyt korzystna zlozonoscia
Polega na przejsciu przez tablice o dlugosci 'n', 'n' razy
za kazdym razem porownujac pary elementow i zamieniajac
miejscami jesli wiekszy jest przed mniejszym
'''

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [1, 7, 2, 9, 0, 0, 8, 9, 3, 4]
print(bubble_sort(arr))