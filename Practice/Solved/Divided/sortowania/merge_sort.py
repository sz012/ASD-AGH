#O(nlogn)
def merge_sort(T):
    if len(T) > 1:
        lT = T[:len(T)//2] #lewa strona
        rT = T[len(T)//2:] #prawa strona

        merge_sort(lT) #rekurencja lewej
        merge_sort(rT) #rekurencja prawej

        i = 0 #lT idx
        j = 0 #rT idx
        k = 0 #new aray idx
        while i < len(lT) and j < len(rT):
            if lT[i] < rT[j]:
                T[k] = lT[i]
                i += 1
            else:
                T[k] = rT[j]
                j += 1
            k += 1
        while i < len(lT):
            T[k] = lT[i]
            i += 1
            k += 1
        while j < len(rT):
            T[k] = rT[j]
            j += 1
            k += 1
#test  
T = [2, 2, 5, 1, 0, 0, 8, 9, 3, 1, 0]
merge_sort(T)
print(T)

