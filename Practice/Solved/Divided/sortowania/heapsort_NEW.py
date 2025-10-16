'''
O(nlogn)
Sortowanie przez kopcowanie, z drzewem binarnym (korzen ma co najw 2 dzieci)
Algorytm posiada akceptowalna zlozonosc
Tworzymy 'maksymalne' drzewo binarne, a nastepnie sortujemy dane
zamieniajac najwiekszy element z ostatnim (najwiekszy juz znika) i ponownie za kazdym razem
tworzac nowe 'maksymalne' drzewo binarne
'''

def heapify(arr, i, upper):
    while True:
        left = i*2 + 1
        right = i*2 + 2

        if max(left, right) < upper:
            if arr[i] >= max(arr[left], arr[right]):
                break
            elif arr[left] > arr[right]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
        elif left < upper:
            if arr[left] > arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                break
        elif right < upper:
            if arr[right] > arr[i]:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
            else:
                break
        else:
            break

def heapsort(arr):
    for j in range((len(arr)-2)//2, -1, -1):
        heapify(arr, j, len(arr))

    for end in range(len(arr)-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, 0, end)

arr = [6, 4, 2, 0, 8, 5, 2, 1, 9, 9, 1]
heapsort(arr)
print(arr)
