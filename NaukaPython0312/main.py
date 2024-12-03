# Skladnia itp.

#Tworzenie zmiennych

zm1 = 1
zm2 = "Zmienna 2"
zm3 = 0.5
zm4 = True

#Wyświetlanie zmiennych/jakiegoś napisu w konsoli

print("Fajne zmienne ;)")
print(zm1)
print(zm2)
print(zm3)
print(zm4)

#Input

inp1 = int(input("Podaj jakąś liczbę: "))
print(inp1)

#Tablice i ich funkcje

warzywa = ["pomidor", "marchew", "ziemniak", "kalafior", "ogórek"]
print(warzywa) #wypisuje całą tablicę
print(warzywa[0]) #wypisuje element z tablicy o indeksie 1
print(warzywa[1:]) #wypisuje elementy z tablicy od indeksu 2 do końca
print(warzywa[-1]) #wypisuje ostatni element z tablicy
warzywa.append("burak") #dodaje element do tablicy
print("Tablica z dodanym elementem:", warzywa)
warzywa.remove("ziemniak") #usuwa wybrany element z tablicy
print("Tablica z usuniętym elementem",warzywa)
for warzywo in warzywa: #iteracja przez tablicę
    print(warzywo)

# Instrukcje warunkowe (if, elif, else), >, <, >=, <=, == !=

#Przykład: Sprawdzanie czy osoba jest pełnoletnia
print("Czy jesteś pełnoletni?")
wiek = int(input("Podaj swój wiek: "))
print("Podany wiek:", wiek)
if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś pełnoletni.")

#Pętle (for, while)

#for - iteracja po elementach sekwencji (np. lista, krotka, ciąg znaków).
#Przykład: Program liczby ile jest danych znaków w ciągu.

ciag = input("Podaj jakiś ciąg znaków: \n")
znak_do_liczenia = input("Podaj jakąś literę, którą chcesz sprawdzić: \n")

licznik = 0
for znak in ciag:
    if znak == znak_do_liczenia:
        licznik += 1

print(f"Znak '{znak_do_liczenia}' występuje {licznik} razy w ciągu.")

#while - wykonuje się, dopóki warunek jest prawdziwy.
#Przykład: Zwiększenie wartości count o 1
count = 0
while count < 23:
    print(count)
    count += 1 #Wyświetlają się liczby od 0 do 22

#Funkcje (def)

#Przykład: Obliczanie sumy dwóch liczb

def suma(a, b): #deklarowanie funkcji poprzez "def", nazwę, oraz argumenty
    wynik = a + b
    return wynik

# Wywołanie funkcji
liczba1 = int(input("Podaj liczbę a: "))
liczba2 = int(input("Podaj liczbę b: "))
suma_liczb = suma(liczba1, liczba2)
print(f"Suma liczb {liczba1} i {liczba2} wynosi {suma_liczb}.")

#funkcje wbudowane python
#len() - zwraca długość obiektu (listy, ciągu znaków)
tekst = "Python to świetny język programowania"
print(f"Tekst '{tekst}' posiada {len(tekst)} znaków.")

#type() - zwraca typ obiektu
liczba = 10
print(type(liczba))
liczba = 0.5
print(type(liczba))
tekst = "Małpa"
print(type(tekst))
wartosc = True
print(type(wartosc))

#round() - zaokrągla liczbę do określonej liczby miejsc
liczba = 3.14159
print(round(liczba, 2))

#max() - zwraca największy element z sekwencji (listy, krotki) lub wielu argumentów.
liczby = [123,-213,4,1,676,122,45,78,2,-1]
print(max(liczby))

#min() - zwraca najmniejszy element z sekwencji lub wielu argumentów.
liczby = [123,-213,4,1,676,122,45,78,2,-1]
print(min(liczby))

#sum() - zwraca sumę wszystkich elementów w iterowalnym obiekcie.
liczby = [123,-213,4,1,676,122,45,78,2,-1]
print(sum(liczby))

#range() tworzy iterowalny obiekt w postaci ciągu liczb. Często używane w pętlach for.
for i in range(10):
    print(i)

#sorted() - zwraca nową posortowaną listę
liczby = [3, 1, 4, 1, 5, 9]
print("Nieposortowana: ", liczby)
print("Posortowana: ",sorted(liczby))

#reversed() - zwraca odwrócony itelator z elementów sekwencji
liczby = [1, 2, 3, 4]
print("Nieodwrócone: ", liczby)
print("Odwrócone: ",list(reversed(liczby)))



