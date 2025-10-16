'''
O(nlogn)
Sortowanie przez scalanie
Jedna z czestszych metod sortowania z korzystna zlozonoscia
Ma dodatkowe zastosowania takie jak znalezienie ilosci
inwersji w tablicy
Polega na rekurencyjnym rozdzielaniu tablicy na pol
a nastepnie stopniowym laczeniu jej z powrotem
w odpowiedniej kolejnosci
'''

def merge_sort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
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

arr = [2, 1, 3, 4, 0, 9, 8]
merge_sort(arr)
print(arr)