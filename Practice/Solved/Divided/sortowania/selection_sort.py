#O(n^2) PROSTY
def selection_sort(T):
    if len(T) > 1:
        for i in range(len(T)): #iterator przechodzi po każdym elemencie tablicy
            cur_min_idx = i #ta zmienna bedzie wyznaczać najmniejszy element tablicy w każdej iteracji
            for j in range(i + 1, len(T)): #drugi iterator szuka najmniejszego elementu w reszcie tablicy
                if T[j] < T[cur_min_idx]:
                    cur_min_idx = j
            T[i], T[cur_min_idx] = T[cur_min_idx], T[i] #oraz ustawia liczbę na końcu posortowanej części

T = [9, 2, 5, 10, 2, 0]
selection_sort(T)
print(T)