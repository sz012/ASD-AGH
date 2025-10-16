'''
O(n^2)
Prosty kod, z duza zlozonoscia
Idac indeksami w gore za kazdym razem poszukujemy
najmniejszego elementu tablicy i zamieniamy go miejscem
z przedmiotem przypisanym do indeksu pierwszego iteratora
'''

def selection_sort(arr):
    for i in range(len(arr)):
        curMinIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curMinIdx]:
                curMinIdx = j
        arr[i], arr[curMinIdx] = arr[curMinIdx], arr[i]

    return arr

arr = [4, 3, 2, 7, 5, 1, 0, 9]
print(selection_sort(arr))

