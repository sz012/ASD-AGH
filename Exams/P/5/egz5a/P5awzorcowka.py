from egzP5atesty import runtests

def inwestor ( T ):
    n = len(T)
    if n == 0:
        return 0

    # L[i] przechowuje indeks pierwszego elementu na lewo od i, który jest mniejszy od T[i]
    # R[i] przechowuje indeks pierwszego elementu na prawo od i, który jest mniejszy od T[i]
    L = [-1] * n
    R = [n] * n
    stack = []

    # Obliczanie R (następny mniejszy element)
    for i in range(n):
        while stack and T[stack[-1]] > T[i]:
            R[stack.pop()] = i
        stack.append(i)

    stack = [] # Czyszczenie stosu

    # Obliczanie L (poprzedni mniejszy element)
    for i in range(n - 1, -1, -1):
        while stack and T[stack[-1]] > T[i]:
            L[stack.pop()] = i
        stack.append(i)

    max_profit = 0
    for i in range(n):
        # Długość przedziału, w którym T[i] jest minimum
        width = R[i] - L[i] - 1
        max_profit = max(max_profit, T[i] * width)

    return max_profit

runtests ( inwestor, all_tests=True )