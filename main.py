ciagJeden = [45, 213,765, 23, 67,23, 87, 1]
ciagDwa = [100, 76, 24, 56, 12, 99, 234, 123]
ciagTrzy= [1243, 546,21, 1, 234, 65, 2]
print("Ciągi przed zmianą: \n", "ciąg jeden: ", ciagJeden, ", ciąg dwa: ", ciagDwa, ", ciąg trzy: ", ciagTrzy)

# Zmiana liczb nieparzystych na 1

print("Zmiana liczb nieparzystych na 1: ")
def nieparzyste_na_jedynki(lista):
    lista_zmieniona = []
    for liczba in lista:
        if liczba % 2 != 0:
            lista_zmieniona.append(1)
        else:
            lista_zmieniona.append(liczba)
    return lista_zmieniona

print(nieparzyste_na_jedynki(ciagJeden))
print(nieparzyste_na_jedynki(ciagDwa))
print(nieparzyste_na_jedynki(ciagTrzy))

# Dzielenie ciągu na liczby parzyste i nie parzyste (dodanie do osobnych list)
print("Podział ciągu na listy z parzystymi i nieparzystymi liczbami: ")
def nieparzyste_i_parzyste(lista):
    parzyste = []
    nieparzyste = []
    for liczba in lista:
        if liczba % 2 == 0:
            parzyste.append(liczba)
        else:
            nieparzyste.append(liczba)
    return "Liczby parzyste:", parzyste, "Liczby nieparzyste:", nieparzyste

print(nieparzyste_i_parzyste(ciagJeden))
print(nieparzyste_i_parzyste(ciagDwa))
print(nieparzyste_i_parzyste(ciagTrzy))

# Uporządkowanie malejące
print("Porządkowanie malejąco: ")
def malejaco(lista):
    for i in range(len(lista) - 1):
        if lista[i] <= lista[i + 1]:
            return False
    return True

print(malejaco(ciagJeden))
print(malejaco(ciagDwa))
print(malejaco(ciagTrzy))