"""
Szymon Pytel
Pomysł polega na zastosowaniu strategii zachłannej: staramy się osiągnąć jak najmniej cięć przez dotarcie
do jak najdłuższej końcowej deski.
W tym celu sprawdzamy dwa przypadki:
1) Dominującym jest cięcie z góry i od niego zaczynamy
2) Dominującym jest cięcie z lewej i od niego zaczynamy
Staramy się ciąć najpierw z dominującej strony, ile się da, a potem, kiedy już nie damy rady dalej, próbujemy ciąć
z drugiej strony. I po takim próbnym cięciu sprawdzamy, czy dalej nie da się ciąć z dominującej strony (i tak w kółko)
Rozwiązanie gwarantuje złożoność wzorcową O(n + m)
"""

from kol3testy import runtests


def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])

    # Cięcie z góry
    hori = 0
    x = 0
    y = 0

    while True:
        if y == n - 1 and C[y][x] <= s:
            # Końcowa deska - dłuższa (dobra ilość sęków)
            break

        if y == n - 1 and x == m - 1:
            # Końcowa deska (ostateczna 1x1)
            if C[y][x] > s:
                # Zła ilość sęków - nie ma rozwiązania
                hori = float('inf')
            break

        if y == n - 1 and C[y][x] > s:
            # Końcowa deska (zła liczba sęków)
            if C[y][x] - C[y][x + 1] > s:
                # Nie da się ciąć z lewej
                hori = float('inf')
                break
            else:
                x += 1
        else:
            # Deska gdzieś w trakcie cięcia
            if C[y][x] - C[y + 1][x] <= s:
                # Da się ciąć z góry
                y += 1
            else:
                if C[y][x] - C[y][x + 1] > s:
                    # Nie da się ciąć z lewej
                    hori = float('inf')
                    break
                else:
                    x += 1

        hori += 1

    # Cięcie z lewej

    vert = 0
    x = 0
    y = 0

    while True:
        if x == m - 1 and C[y][x] <= s:
            break

        if x == m - 1 and y == n - 1:
            if C[y][x] > s:
                vert = float('inf')
            break

        if x == m - 1 and C[y][x] > s:
            if C[y][x] - C[y + 1][x] > s:
                vert = float('inf')
                break
            else:
                y += 1
        else:
            if C[y][x] - C[y][x + 1] <= s:
                x += 1
            else:
                if C[y][x] - C[y + 1][x] > s:
                    vert = float('inf')
                    break
                else:
                    y += 1

        vert += 1

    if vert == float('inf') and hori == float('inf'):
        return -1

    return min(hori, vert)


runtests(parkiet, all_tests = False)