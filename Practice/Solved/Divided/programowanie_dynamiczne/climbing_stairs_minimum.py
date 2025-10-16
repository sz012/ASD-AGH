# Naszym zadaniem jest znalezienie minimalnej kwoty jaką musimy zapłacić, aby przejść po schodach.
# W każdym kroku możemy przejść o 1 lub 2 schody w górę.
# W każdym kroku musimy zapłacić kwotę równą wysokości schodów, na które wchodzimy.
# Ceny schodów jest podana w tablicy `cost`.



def climbing_stairs_minimum(cost):
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])