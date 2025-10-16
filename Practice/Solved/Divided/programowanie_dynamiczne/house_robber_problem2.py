# Naszym zadaniem jest najbardziej oplacalnie dla zlodzieja wybrac domy do obrabowania
# Zasada jest taka ze nie mozna wkrasc sie do zadnych obok siebie, A DOMY LEZA W OKREGU
# Zysk po kradziezy konkretnego domu wystepuje w tablicy houses

T = [2, 5, 6, 2, 7, 3, 3, 2, 9, 1]

def house_robber_problem2(houses):
    rob1, rob2 = 0, 0
    for i in range(len(houses)):
        houses[i] = max(rob1 + houses[i], rob2)
        rob1 = rob2
        rob2 = houses[i]

    return rob2

print(max(house_robber_problem2(T[1:]), house_robber_problem2(T[:-1])))