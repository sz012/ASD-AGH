#O(nlogn)
def heapify(T, i, upper):
    while True:
        l = i*2 + 1
        r = i*2 + 2

        if max(l, r) < upper:
            if T[i] >= max(T[l], T[r]) :
                break
            elif T[l] > T[r]:
                T[i], T[l] = T[l], T[i]
                i = l
            else:
                T[i], T[r] = T[r], T[i]
                i = r
        elif l < upper:
            if T[l] > T[i]:
                T[i], T[l] = T[l], T[i]
                i = l
            else:
                break
        elif r < upper:
            if T[r] > T[i]:
                T[i], T[r] = T[r], T[i]
                i = r
            else:
                break
        else:
            break

def heapsort(T):
    for j in range((len(T)-2)//2, -1, -1):
        heapify(T, j, len(T))

    for end in range(len(T) - 1, 0, -1):
        T[0], T[end] = T[end], T[0]
        heapify(T, 0, end)

T = [9, 5, 3, 9, 0, 1, 6]
heapsort(T)
print(T)

