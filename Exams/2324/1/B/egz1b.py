'''
Szymon Pytel
Mamy tutaj podana tablice i liczbe k, ktora definiuje ile maksymalnie mozemy usunac elementow
z podciagu aby otrzymac jak najwyzsza sume
Zadaniem programu jest znalezc ta najwyzsza sume, a co za tym idzie najbardziej korzystny podciag
gdzie mozemy usunac maksymalnie k elementow
Moim pomyslem na ten moment jest wykonac trzy petle, iteratory i oraz j ida od koncow tablicy a k
liczy ilosc usunietych elementow
'''
from egz1btesty import runtests

def kstrong(T, k):
  n = len(T)
  maxSum = -float('inf')
  for i in range(n):
    for j in range(n, i, -1):
      newT = sorted(T[i:j])
      l = 0
      ctr = k
      while l < len(newT):
        if ctr > 0 and newT[l] < 1:
          newT[l] = 0
          ctr -= 1
        l += 1
      maxSum = max(maxSum, sum(newT))
  return maxSum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )
