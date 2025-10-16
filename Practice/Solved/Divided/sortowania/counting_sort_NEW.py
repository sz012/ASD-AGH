'''
O(k)
Tutaj k to najwieksza wartosc elementu
Counting sort dziala dobrze gdy zakres elementow czyli najwieksza wystepujaca
wartosc nie jest duzo wieksza od ilosci elementow
Dane powinny rowniez byc liczbami calkowitymi nieujemnymi
Dla liczb ujemnych trzeba by go odpowiednio dostosowac
Algorytm polega na zliczaniu ilosci wystapien danych elementow i ustawianiu ich obok siebie
'''

def counting_sort(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)

    return sorted_arr

arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
