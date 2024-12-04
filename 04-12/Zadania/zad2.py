# Napisz program, który znajdzie maksymalną wartość, jaką można uzyskać,
# pakując przedmioty o różnych wartościach i wagach w plecak o ograniczonej pojemności.
# Użyj algorytmu zachłannego.

def plecak(przedmioty, pojemnosc):
    max_wartosc = 0
    waga_aktualna = 0
    przedmioty_w_plecaku = []
    for waga, wartosc in przedmioty:
        if waga_aktualna + waga <= pojemnosc:
            waga_aktualna += waga
            max_wartosc += wartosc
            przedmioty_w_plecaku.append((waga, wartosc))
        else:
            break
    return max_wartosc, przedmioty_w_plecaku

przedmioty = [(10, 60), (20, 100), (30, 120)]
pojemnosc = 50

max_wartosc, przedmioty_w_plecaku = plecak(przedmioty, pojemnosc)

print(f'Maksymalna wartość w plecaku: {max_wartosc}')
print(f'Przedmioty w plecaku: {przedmioty_w_plecaku}')