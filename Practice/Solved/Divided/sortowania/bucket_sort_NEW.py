'''
O(n+k)
Wyjatkowy algorytm ktory w najlepszym przypadku
zadziala ze zlozonoscia liniowa
Wykorzystywany jest do przypadkow gdzie dzialamy na ulamkach mniejszych od 1
rozlozonych w mniej wiecej rownych odstepach
Stoujemy w nim insertion sort aby ulozyc odpowiednio elementy
w kazdym z kubelkow
Dziala dobrze gdy wartosci sa rozlozone rownomiernie
oraz naturalnie grupuja sie do kubelkow
Jezeli sa silne skupione, wszystkie spadaja do jednego
wowczas mamy sortowanie wenatrz czesto o zlozonosci kwadratowej
'''

def insertion_sort(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1

    return arr

def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]

    for element in arr:
        buckets[int(len(arr) * element)].append(element)

    for bucket in buckets:
        insertion_sort(bucket)

    idx = 0
    for bucket in buckets:
        for number in bucket:
            arr[idx] = number
            idx += 1

arr = [0.5, 0.1, 0.6, 0.65, 0.9]
bucket_sort(arr)
print(arr)