# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = int(input("Podaj rok: \n"))

if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print("Rok {} jest przestepny.".format(rok))
else:
    print("Rok {} nie jest przestepny.".format(rok))
