def min_l_monet(kwota, monety):
    monety.sort(reverse=True)
    liczba_monet = 0
    pozostala_kwota = kwota

    for moneta in monety:
        if pozostala_kwota == 0:
            break

        if moneta <= pozostala_kwota:
            liczba_monet += pozostala_kwota // moneta
            pozostala_kwota %= moneta

    if pozostala_kwota != 0:
        return -1

    return liczba_monet

monety = [1, 2, 5]
kwota = int(input("Podaj jakąś kwote: "))

wynik = min_l_monet(kwota, monety)
if wynik == -1:
    print("Nie można uzyskać tej kwoty przy użyciu dostępnych monet.")
else:
    print(f"Minimalna liczba monet potrzebna do uzyskania kwoty {kwota} to: {wynik}")