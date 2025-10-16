from egzP2atesty import runtests

def zdjecie(T, m, k):
    """
    Przestawia tablicę T (lista krotek: (id, w)) tak, aby:
      - w każdym wyższym rzędzie była co najmniej jedna osoba wyższa
        niż wszystkie osoby w rzędzie poniżej,
      - każdy był widoczny wg definicji z treści,
      - bez użycia wbudowanych sortowań.
    Numeracja miejsc na zdjęciu jest kolumnami po skosie (jak w szkicu).
    m - liczba rzędów, k - liczba osób w najniższym rzędzie.
    Złożoność: O(n * m) w pesymistycznym wariancie selekcji na poszatkowanym zakresie.
    """
    n = len(T)

    # START[i], END[i] - zakres indeksów (w liniowym buforze miejsc) należących do rzędu i
    # Szerokość rzędów w tej numeracji: m+k-1, m+k-2, ..., k  (suma = n)
    START = [0 for _ in range(m)]
    END = [0 for _ in range(m)]
    aktEND = -1
    aktWIDTH = m + k - 1
    for i in range(m):
        START[i] = aktEND + 1           # początek i-tego rzędu (w buforze miejsc)
        aktEND += aktWIDTH              # koniec i-tego rzędu
        END[i] = aktEND
        aktWIDTH -= 1                   # wyższy rząd ma o 1 „węższy” zakres

    # IND jest permutacją indeksów miejsc: przechodzimy kolumnami po skosie
    # (row od 0 do m-1, następnie col++) i mapujemy to na spójny zakres [0..n-1].
    # Dzięki temu później partiujemy/wybieramy tylko w miejscach „istniejących” na zdjęciu.
    IND = [0 for _ in range(n)]
    items = 0
    col = 0
    row = 0
    while items < n:
        # jeśli w danym rzędzie istnieje miejsce o przesunięciu 'col', przypisz je
        if START[row] + col <= END[row]:
            IND[START[row] + col] = items
            items += 1
        row += 1
        if row >= m:                    # przeskok do kolejnej „kolumny po skosie”
            row = 0
            col += 1

    # Selekcja od dołu do góry:
    # Po wywołaniu quickselect z k = END[i] pivot ląduje dokładnie na granicy rzędu i
    # i jest najmniejszym z elementów po jego lewej (porządek malejący po w),
    # co gwarantuje „przebicie” wysokością względem niższego rzędu bez pełnego sortowania.
    lastEND = END[m - 1]                # początkowo obejmujemy do końca najniższego rzędu
    for i in range(m - 2, -1, -1):      # od przedostatniego rzędu do pierwszego
        quickselect(T, IND, 0, END[i], lastEND)
        lastEND = END[i] - 1            # zawężamy prawą granicę na potrzeby wyższych rzędów

    return None


def partition(T, IND, p, r):
    """
    Partiowanie wg pivota na pozycji r (w porządku malejącym po wzroście).
    Operujemy tylko na miejscach T wskazanych przez wycinek IND[p..r].
    Zwraca indeks q taki, że:
      - wszystkie pozycje w IND[p..q] mają w >= pivot,
      - wszystkie w IND[q+1..r] mają w < pivot.
    """
    pivot = T[IND[r]][1]                # wzrost pivota
    i = p - 1
    for j in range(p, r):
        if T[IND[j]][1] >= pivot:       # „malejąco”: większe idą na lewo
            i += 1
            T[IND[j]], T[IND[i]] = T[IND[i]], T[IND[j]]
    T[IND[i + 1]], T[IND[r]] = T[IND[r]], T[IND[i + 1]]
    return i + 1


def quickselect(T, IND, p, k, r):
    """
    Selekcja częściowa (odmiana Quickselect) na poszatkowanym zakresie:
    - p..r: pracujemy na miejscach z IND[p..r],
    - k: docelowa pozycja pivota po partiowaniu (liczona w przestrzeni IND).
    Zapewnia, że element na pozycji k (w sensie IND) będzie na swoim „miejscu”,
    a po lewej będą elementy o w >= niego (malejąco).
    """
    if p < r:
        q = partition(T, IND, p, r)
        if q > k:
            quickselect(T, IND, p, k, q - 1)
        elif q < k:
            quickselect(T, IND, q + 1, k, r)
    return


runtests(zdjecie, all_tests=False)