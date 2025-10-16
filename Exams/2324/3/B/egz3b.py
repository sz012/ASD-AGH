'''
Szymon Pytel
Zadanie polega na znalezieniu jak najdluzszego spojnego podciagu tablicy ktory zawiera
maksymalnie dwie liczby k-pechowe
Liczba k-pechowa to element ciagu ktorego wzor rekurencyjny podany mamy w poleceniu,
wykorzystuje on oczywiscie zmienna k
Funkcja kunlucky ma zwrocic dlugosc tego fragmentu
Moim pomyslem jest na biezaco, idac prawym wskaznikiem po liscie sprawdzac
czy elementy naleza do uprzednio utworzonego w osobnej funkcji pechowego ciagu oraz
w przypadku zwiekszenia ilosci k-pechowych liczb przesuwac lewy wskaznik
Istotna czesc kodu to jednoczesne zamienianie liczb na wartosci logiczne (czy sa pechowe)
przez wskaznik r, w tej samej tablicy
W odpowiednich momentach dlugosc podciagu porownujemy z najwieksza do tej pory znaleziona
Program dziala z najlepsza zlozonoscia - liniowa
'''
from egz3btesty import runtests

def gen_kunlucky_set(T, k, max_num):
  kset = set()
  x = k
  i = 1

  while x <= max_num:
    kset.add(x)
    x = x + (x % i) + 7
    i += 1
  return kset

def kunlucky(T, k):
  kset = gen_kunlucky_set(T, k, max(T))

  l, r = 0, 0
  cnt, tmp_len, max_len = 0, 0, 0

  while r < len(T):

    if cnt < 3:
      T[r] = T[r] in kset  # 1 lub 0
      tmp_len += 1
      cnt += T[r]
      r += 1
      if cnt < 3 and max_len < tmp_len:
        max_len = tmp_len
    else:
      tmp_len -= 1
      cnt -= T[l]
      l += 1
  return max_len


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = False)
