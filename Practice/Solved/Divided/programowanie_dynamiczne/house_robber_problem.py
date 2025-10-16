# Naszym zadaniem jest najbardziej oplacalnie dla zlodzieja wybrac domy do obrabowania
# Zasada jest taka ze nie mozna wkrasc sie do zadnych obok siebie
# Zysk po kradziezy konkretnego domu wystepuje w tablicy houses

def house_robber_problem(houses):
    rob1, rob2 = 0, 0
    for i in range(len(houses)):
        houses[i] = max(rob1 + houses[i], rob2)
        rob1 = rob2
        rob2 = houses[i]

    return rob2


