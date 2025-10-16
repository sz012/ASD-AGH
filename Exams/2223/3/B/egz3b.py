'''
Szymon Pytel

W tablicy P podane mamy przedzialy domkniete i naszym zadaniem jest napisac funkcje
ktora jak najszybciej znajdzie pare przedzialow ktore ani sie w sobie nie zawieraja, ani nie sa rozlaczne
Innymi slowy mamy jak najszybciej znalezc przedzialy nachodzace na siebie, ale niezupelnie.
To co przychodzi od razu na mysl gwarantuje wysoka zlozonosc
Aby przejsc do lepszej zlozonosci nalezy posortowac tablice i uzyc metody sweep line
'''
from egz3btesty import runtests

def uncool(P):
    n = len(P)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a1, b1 = P[i]
            a2, b2 = P[j]
            if not (b1 < a2 or b2 < a1):
                if not ((a1 <= a2 and b2 <= b1) or (a2 <= a1 and b1 <= b2)):
                    return (i, j)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = False )
