'''
Szymon Pytel
Mamy tablice wyborow w ktorej kazdy zawiera okregi i ich wyborcow, koszta kampanii oraz dostepne fundusze
Zadanie polega na tym aby z kazdych wyborow wybrac okregi w ktore zainwestujemy dysponujac okreslona
iloscia funduszy na jedne wybory i zebrac jak najwiecej glosow ktorych ilosc jest okreslona w poszczegolnych okregach
Zadanie mozna splycic do zlozonego knapsack problem gdzie uzywamy algorytmu plecakowego
kilka razy i sumujemy wyniki
Jest to jeden z najlatwiejszych algorytmow dynamicznych, trudnosc polega na tym
ze operujemy na liscie jednokierunkowej, co oznacza ze dla wlasciwego dzialania programu
nalezy zebrac wszystkie okregi wyborcze do jednej listy
'''
from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    suma = 0
    for wyb in T:
        nodes = []
        node = wyb
        while node:
            nodes.append(node)
            node = node.next
        n = len(nodes)
        fundusze = wyb.fundusze
        dp = [[0] * (fundusze + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for fun in range(fundusze + 1):
                if nodes[i-1].koszt > fun:
                    dp[i][fun] = dp[i-1][fun]
                else:
                    dp[i][fun] = max(dp[i-1][fun], dp[i-1][fun - nodes[i-1].koszt] + nodes[i-1].wyborcy)
        suma += dp[n][fundusze]
    return suma

runtests(wybory, all_tests = True)