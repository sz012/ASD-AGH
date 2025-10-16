#sortowanie przez wstawianie
#zlozonosc O(n^2)
dTablicy = int(input('Podaj dlugosc tablicy: '))
T = []
for element in range(dTablicy):
    e = int(input(f'Podaj {element + 1}-ty element: ', ))
    T.append(e)

def SPW(T):
    n = len(T)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if T[j] < T[j-1]:
                T[j], T[j-1] = T[j-1], T[j]
            else:
                break
    return T

print(SPW(T))