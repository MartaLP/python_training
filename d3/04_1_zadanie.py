# 1. czy liczba jest podzielna przez 3 lub 5 lub 7

liczba = float(input("Podaj liczbe: \n"))

if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7 == 0:
    print("Liczba {} jest podzielna przez 3 lub 5 lub 7".format(liczba))
else:
    print("Liczba {} nie jest podzielna przez 3, 5 lub 7".format(liczba))
