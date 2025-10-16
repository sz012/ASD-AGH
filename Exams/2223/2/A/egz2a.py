'''
Szymon Pytel

Algorytm o złożoności O(n log n) opiera się na posortowaniu wszystkich punktów rosnąco według współrzędnej x.
Dzięki temu, przetwarzając punkty w tej kolejności, dla każdego z nich mamy pewność, że wszystkie wcześniej rozpatrzone punkty
mają mniejszą lub równą współrzędną x. Problem sprowadza się więc do szybkiego zliczania,
ile z tych wcześniejszych punktów ma jednocześnie mniejszą współrzędną y.
Do tego celu wykorzystywana jest struktura danych zwana Drzewem Fenwicka, która pozwala na zliczanie takich punktów
w czasie logarytmicznym. Algorytm iteruje po posortowanych punktach, dla każdego z nich wykonując zapytanie
do drzewa o jego siłę, a następnie aktualizując drzewo o własną pozycję.

Wersja algorytmu dążąca do złożoności liniowej O(n) eliminuje standardowe sortowanie porównawcze,
które jest głównym źródłem czynnika log n. Wykorzystuje ona fakt, że współrzędne pochodzą z ograniczonego zbioru {1, ..., n},
co pozwala na zastosowanie sortowania kubeczkowego (bucket sort) w czasie liniowym.
Punkty są grupowane w "kubeczkach" odpowiadających ich współrzędnej x, a następnie kubeczki są przetwarzane
w rosnącej kolejności. Mimo że sortowanie jest liniowe, do zliczania punktów dominowanych wciąż używane jest Drzewo Fenwicka,
którego operacje mają koszt logarytmiczny. Z tego powodu ostateczna złożoność algorytmu pozostaje O(n log n),
jednak jest to najszybsze praktyczne podejście do tego problemu.
'''
from egz2atesty import runtests


# Implementacja Drzewa Fenwicka (Binary Indexed Tree)
class FenwickTree:
  def __init__(self, size):
    # Drzewo jest 1-indeksowane, więc potrzebujemy size+1
    self.tree = [0] * (size + 1)

  def update(self, index, value):
    """Dodaje 'value' do elementu o indeksie 'index'."""
    # Współrzędne są od 1 do n, więc pasują do 1-indeksowania
    while index < len(self.tree):
      self.tree[index] += value
      index += index & (-index)

  def query(self, index):
    """Zwraca sumę prefiksu do indeksu 'index' włącznie."""
    s = 0
    while index > 0:
      s += self.tree[index]
      index -= index & (-index)
    return s


def dominance(P):
  """
  Oblicza siłę najsilniejszego punktu w złożoności O(n log n).
  """
  if not P:
    return 0

  n = len(P)

  # Krok 1: Posortuj punkty
  # Sortujemy rosnąco po x, a dla równych x, rosnąco po y.
  P.sort()

  # Krok 2: Inicjalizacja struktury danych i zmiennych
  # Współrzędne są z {1...n}, więc rozmiar drzewa to n.
  bit = FenwickTree(n)
  max_strength = 0

  i = 0
  while i < n:
    # Znajdź grupę punktów z tą samą współrzędną x
    j = i
    while j < n and P[j][0] == P[i][0]:
      j += 1

    # Krok 3a: Oblicz siłę dla każdego punktu w grupie
    # Robimy to PRZED dodaniem ich do drzewa, bo punkty o tym samym x
    # nie mogą się wzajemnie dominować.
    for k in range(i, j):
      px, py = P[k]
      # Siła to liczba punktów (x', y') z x' < px i y' < py.
      # Ponieważ punkty są posortowane po x, wszystkie punkty
      # już w drzewie mają x' <= px. Przez przetwarzanie grupowe
      # zapewniamy, że te w drzewie mają x' < px.
      # Potrzebujemy więc tylko policzyć, ile z nich ma y' < py.
      strength = bit.query(py - 1)
      if strength > max_strength:
        max_strength = strength

    # Krok 3b: Dodaj wszystkie punkty z grupy do drzewa
    for k in range(i, j):
      px, py = P[k]
      bit.update(py, 1)

    # Przejdź do następnej grupy
    i = j

  return max_strength

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
