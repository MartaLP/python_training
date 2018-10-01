# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R, 2B):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta


wynik = "19B "
wynik = wynik.strip()

typ=wynik[-1]
liczba=int(wynik[:-1])

lista=[]

if typ=="R":
    lista.append("Czerwona")
else:
    lista.append("Czarna")

if liczba > 18:
    lista.append("Wysoka")
else:
    lista.append("Niska")

if liczba % 2 == 0:
    lista.append("Parzysta")
else:
    lista.append("Nieparzysta")

print(lista)