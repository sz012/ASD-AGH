'''
Szymon Pytel
Moim pomyslem jest wykorzystac strukture stack i iterujac po tablicy dodawac kolejne elementy
Jesli trafimy na liczbe wieksza lub rowna niz poprzednia, w kolejnej petli usuwamy ze stosu liczby mniejsze od niej
wiedzac ze dochadzac do wiekszej reszte mozemy zignorowac
Waznym jest aby ocenic czy liczba jest nie na swoim miejscu - jesli tak, nalezy pozbyc sie rowniez i niej
Zlozonosc rozwiazania to O(n)

ZAKOMENTOWANE KODY NIE SA DO OCENY!!!
'''
from egz2Btesty import runtests
'''
def bitgame_idea1(T):
    ctr = 0
    for i in range(1, len(T)):
        if T[i-1] != float('inf') and T[i] < T[i-1]:
            continue

        bad = False
        for j in range(i-1, -1, -1):
            if T[j] != float('inf') and T[j] > T[i]:
                break
            if T[j] != float('inf') and T[j] <= T[i]:
                bad = True
                ctr += 1
                T[j] = float('inf')
        if bad:
            ctr += 1
            T[i] = float('inf')

    return len(T) - ctr
'''
'''
def bitgame_idea2(T):
    ctr = 0
    for i in range(1, len(T)):
        if T[i-1] != float('inf') and T[i] < T[i-1]:
            continue
        if T[i-1] == float('inf') and T[i] < T[i-length]:
            continue

        bad = False
        for j in range(i-1, -1, -1):
            if T[j] > T[i]:
                break
            if T[j] != float('inf') and T[j] <= T[i]:
                bad = True
                ctr += 1
                T[j] = float('inf')
        if bad:
            ctr += 1
            T[i] = float('inf')
            length = i - j

    return len(T) - ctr
'''
def bitgame(T):
    stack = []
    for el in T:
        bad = False
        while stack and stack[-1] <= el:
            stack.pop()
            bad = True
        if bad:
            continue
        stack.append(el)
    return len(stack)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( bitgame, all_tests = False )
