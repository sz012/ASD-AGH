from typing import List, TypeVar, MutableSequence

T = TypeVar("T")


def partition(arr: MutableSequence[T], left: int, right: int) -> int:
    """
    Partiowanie wg schematu Lomuto.
    Przestawia elementy tak, by:
      - wszystkie <= pivot były po lewej,
      - wszystkie > pivot były po prawej,
      - pivot trafił na swoją ostateczną pozycję i został zwrócony jej indeks.
    Operuje na przekroju [left, right] (obie granice włącznie).
    """
    # 1) Wybór pivota: weź ostatni element jako pivot
    pivot = arr[right]

    # 2) i pokazuje miejsce w które wstawimy kolejny element <= pivot
    i = left

    # 3) Przejdź po wszystkich elementach poza pivotem
    for j in range(left, right):
        # 4) Jeśli bieżący element jest <= pivot,
        #    to powinien znaleźć się w części "mniejszej lub równej" po lewej
        if arr[j] <= pivot:
            # 5) Zamień arr[i] z arr[j], aby dobudować lewy segment
            arr[i], arr[j] = arr[j], arr[i]
            # 6) Przesuń granicę lewego segmentu o 1 w prawo
            i += 1

    # 7) Po pętli elementy w [left, i-1] są <= pivot,
    #    więc wstaw pivot na miejsce i (jego właściwa pozycja)
    arr[i], arr[right] = arr[right], arr[i]

    # 8) Zwróć ostateczną pozycję pivota
    return i


def quickselect(arr: MutableSequence[T], k: int, left: int = 0, right: int | None = None) -> T:
    """
    Zwraca k-ty najmniejszy element tablicy (0-indeksowane k).
    Działa in-place, modyfikując arr.
    Średnio O(n), w najgorszym O(n^2).
    """
    # 1) Ustal prawą granicę, jeśli nie podana
    if right is None:
        right = len(arr) - 1

    # 2) Walidacja wejścia: puste dane lub k poza zakresem
    if not (0 <= k < len(arr)):
        raise ValueError("Parametr k musi być w zakresie [0, len(arr)-1].")

    # 3) Iteracyjnie zawężaj przedział wyszukiwania
    while left <= right:
        # 4) Rozdziel przedział wokół pivota i pobierz jego pozycję
        pivot_pos = partition(arr, left, right)

        # 5) Jeśli pivot trafił dokładnie na pozycję k, to znaleźliśmy wynik
        if pivot_pos == k:
            return arr[pivot_pos]
        # 6) Jeśli pivot jest po lewej od k, szukaj w prawej części [pivot_pos+1 .. right]
        elif pivot_pos < k:
            left = pivot_pos + 1
        # 7) W przeciwnym razie szukaj w lewej części [left .. pivot_pos-1]
        else:
            right = pivot_pos - 1

    # 8) Teoretycznie nieosiągalne przy poprawnych danych, ale dla kompletności:
    raise RuntimeError("Nie udało się znaleźć k-tego elementu.")


if __name__ == "__main__":
    # Przykład użycia:
    data: List[int] = [7, 2, 9, 4, 1, 5, 8, 3, 6]

    # k-ty najmniejszy (0-indeksowane): k=0 -> min, k=len-1 -> max
    k = 3  # 4-ty najmniejszy element
    result = quickselect(data, k)

    print(f"k = {k}, k-ty najmniejszy = {result}")
    print(f"Tablica po częściowej reorganizacji: {data}")