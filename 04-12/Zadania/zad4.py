#Napisz program, który będzie wyszukiwał wszystkie wystąpienia zadanego słowa w tekście
# zapisanym w pliku. Program powinien wypisać numery wierszy, w których występuje dane
# słowo oraz indeksy początkowe tego słowa w każdym wierszu. Wyszukiwanie powinno być
# niewrażliwe na wielkość liter i nie powinno uwzględniać interpunkcji.

def znajdz_wystapienia(slowo, nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        wiersze = plik.readlines()

    wynik = []
    for i, wiersz in enumerate(wiersze, start=1):
        indeks = wiersz.lower().find(slowo.lower())
        while indeks != -1:
            wynik.append((i, indeks))
            indeks = wiersz.lower().find(slowo.lower(), indeks + 1)

    for wiersz, indeks in wynik:
        print(f"Wiersz {wiersz}, indeks {indeks}")


znajdz_wystapienia("to", "plik3.txt")


def najczestsze_slowo(nazwa_pliku, nazwa_wynikowego_pliku):
    with open(nazwa_pliku, 'r') as plik:
        tekst = plik.read()

    slowa = []
    for slowo in tekst.split():
        slowo_czyste = ''.join(znak for znak in slowo).lower()
        slowa.append(slowo_czyste)

    licznik = {}
    for slowo in slowa:
        if slowo in licznik:
            licznik[slowo] += 1
        else:
            licznik[slowo] = 1

    najczestsze_slowo = None
    maks_wystapien = 0
    for slowo, wystapienia in licznik.items():
        if wystapienia > maks_wystapien:
            najczestsze_slowo = slowo
            maks_wystapien = wystapienia

    with open(nazwa_wynikowego_pliku, 'w') as wynik:
        wynik.write(f"{najczestsze_slowo}: {maks_wystapien}")

najczestsze_slowo("plik3.txt", "wynik3.txt")