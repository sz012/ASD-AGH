#znajdowanie min i maks w tablicy uzywajac wylacznie 3/2 n porownan (O(3/2 n))
import math

dTablicy = int(input('Podaj dlugosc tablicy: '))
T = []
for element in range(dTablicy):
    e = int(input(f'Podaj {element + 1}-ty element: ', ))
    T.append(e)

min = -math.inf
max = math.inf
# (...)