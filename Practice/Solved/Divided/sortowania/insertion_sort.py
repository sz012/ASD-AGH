#O(n^2) PROSTY
def insertion_sort(T):
    if len(T) > 1:
        for i in range(len(T)): #iterator przechodzi po każdym elemencie tablicy
            j = i
            while j > 0 and T[j-1] > T[j]: #drugi iterator porównuje poprzednie elementy z nowym T[i]
                T[j], T[j-1] = T[j-1], T[j] #oraz ustawia liczbę na odpowiednim miejscu
                j -= 1

T = [2, 4, 1, 2, 0, 8, 9, 8, 0]
insertion_sort(T)
print(T)