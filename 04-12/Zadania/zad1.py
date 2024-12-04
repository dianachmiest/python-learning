#Zaimplementuj algorytm zachłanny, który rozwiązuje problem podziału zbioru.
# Masz zbiór elementów, z których każdy ma przypisaną wartość. Twoim zadaniem jest podzielić
# ten zbiór na dwa podzbiory tak, aby suma wartości elementów w obu podzbiorach była jak
# najbardziej zbliżona. Program powinien działać na danych wczytanych z pliku, gdzie każdy
# element opisany jest wartością.

def podzbiory(plik):
    with open(plik, 'r') as plik_tekstowy:
        liczby = list(map(int, plik_tekstowy.read().split()))
    podzbior1 = []
    podzbior2 = []

    for liczba in liczby:
        if sum(podzbior1) <= sum(podzbior2):
            podzbior1.append(liczba)
        else:
            podzbior2.append(liczba)
    print("Podzbiór 1:", podzbior1, "Suma:", sum(podzbior1))
    print("Podzbiór 2:", podzbior2, "Suma:", sum(podzbior2))


podzbiory("plik1.txt")

