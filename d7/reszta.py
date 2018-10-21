# wydajemy resztę
monety = {5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}

zakupy = 32.30
banknot = 50
reszta = round(banknot - zakupy, 2)
print(f'Reszta do wydania: {reszta:.2f}')
wydano = 0

for moneta in monety.keys():
    if round(reszta, 2) >= moneta:
        il_monet = reszta // moneta
        monety[moneta] = il_monet
        wartosc = il_monet * moneta
        reszta -= wartosc
        print(reszta)
        wydano += wartosc
        print(f'Wydano {il_monet} monet {moneta}')

print(f'Reszta wydana {wydano}')
