'''
Szymon Pytel

W tablicy A podane mamy wielkosci dostaw wegla do nieskonczonej ilosci magazynow
T wyznacza limit kazdego magazynu i wegiel rozdzielamy tak aby pomiescil sie po magazynach
Wazne jest to ze zawsze wybieramy najnizszy mozliwy numer magazynu, a wegiel z kazdej dostawy
ma byc razem

Moim pomyslem na akceptowalna zlozonosc jest stworzyc dwie zagniezdzone petle, gdzie jedna
przechodzi po dostawach a druga szuka dostepnego magazynu i zapisuje jego numer
'''

from egz2atesty import runtests

def coal( A, T ):
    magazines = [0] * len(A)
    for i in range(len(A)):
        for j in range(len(magazines)):
            if A[i] + magazines[j] <= T:
                magazines[j] += A[i]
                save = j
                break
    return save

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
