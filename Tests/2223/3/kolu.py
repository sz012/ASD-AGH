from kolutesty import runtests
# T reprezentuje kubelki lodow, gdzie T[i] to ilosc galek lodow w i-tym kubelku
# Z kazda minuta mozemy zjesc jeden caly kubelek
# Z kazda minuta ilosc lodow w kazdym kubelku maleje o 1
# Ile maksymalnie mozemy zjesc galek lodow zanim wszystkie stopnieja?

def ice_cream( T ):
    T.sort(reverse=True)
    n = len(T)
    sol = 0
    mins = 0

    for i in range(n):
        if T[i] - mins > 0:
            sol += T[i] - mins
            mins += 1
        else:
            break
    return sol
# Wytlumaczenie:
# Sortujemy kubelki malejaco, zeby zaczac od tych z najwieksza iloscia lodow
# W kazdej iteracji sprawdzamy, czy mozemy zjesc jeszcze jakies lody z danego kubelka
# (czy ilosc lodow w kubelku minus liczba minut, ktore juz uplynely, jest wieksza od zera)
# Jesli tak, to dodajemy do wyniku roznice miedzy iloscia lodow w kubelku a liczba minut
# i zwiekszamy liczbe minut o 1 (bo zjemy kubelek)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = False )