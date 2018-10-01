# 3. oblicz ocenę na podstawie progu procentowego

WYNIK = 88

if WYNIK < 20:
    ocena = 2
elif WYNIK < 40:
    ocena = 3
elif WYNIK < 60:
    ocena = 4
else:
    ocena = 5

print("Uzyskana ocena to {}.".format(ocena))

