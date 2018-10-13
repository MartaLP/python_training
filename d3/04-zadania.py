# 1. czy liczba jest podzielna przez 3 lub 5 lub 7

liczba = 30

if liczba % 3 == 0:
    print("Liczba {} jest podzielna przez 3".format(liczba))
if liczba % 5 == 0:
    print("Liczba {} jest podzielna przez 5".format(liczba))
if liczba % 7 == 0:
    print("Liczba {} jest podzielna przez 7".format(liczba))
if (liczba % 3 != 0) and (liczba % 5 != 0) and (liczba % 7 != 0):
    print("Liczba {} nie jest podzielna przez 3, 5 ani 7".format(liczba))

# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400
                                                                                                                        
rok = 2018
if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0):
    print("Rok {} jest przestępny".format(rok))
else:
    print("Rok {} nie jest przestępny".format(rok))

# 3. oblicz ocenę na podstawie progu procentowego
pp = 73

if (pp > 0) and (pp < 30):
    print('Twoja ocena to 1!!! Tragedia!!!')
elif (pp >= 30) and (pp < 50):
    print('Twoja ocena to 2!! Nie jest dobrze.')
elif (pp >= 50) and (pp < 70):
    print('Twoja ocena to 3! Popraw się.')
elif (pp >= 70) and (pp < 90):
    print('Twoja oceana to 4. Jest dobrze.')
elif (pp >= 90) and (pp < 100):
    print('Twoja oceana to 5! Bardzo dobrze.')
elif pp == 100:
    print('Twoja ocena to 6!! Świetnie.')
else:
    print("Błąd")

# 4. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu
miesiac = "Październik"

miasiace_30 = ["Kwiecień", "Czerwiec", "Wrzesień", "Listopad"]

if miesiac == "Luty":
    print("Miesiąc ma 29 dni")
elif miesiac in miasiace_30:
    print("Miesiąc ma 30 dni")
else:
    print("Miesiąc ma 31 dni")

# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

wiosna = ["kwi", "maj"]
lato = ["lip", "sie"]
jesien = ["paz", "lis"]
zima = ["sty", "lut"]
mieszane = ["mar", "cze", "wrz", "gru"]

data = "paz-08"

miesiac = data[0:3]
dzien = int(data[-2:])

if miesiac in wiosna:
    print("Wiosna")
elif miesiac in lato:
    print("Lato")
elif miesiac in jesien:
    print("Jesień")
elif miesiac in zima:
    print("Zima")
elif miesiac in mieszane:
    if miesiac == "mar":
        if dzien >= 20:
            print("Wiosna")
        else:
            print("Zima")
    elif miesiac == "cze":
        if dzien >= 21:
            print("Lato")
        else:
            print("Wiosna")
    elif miesiac == "wrz":
        if dzien >= 22:
            print("Jesień")
        else:
            print("Lat")
    else:
        if dzien >= 21:
            print("Zima")
        else:
            print("Jesień")
else:
    print("Błąd")
    exit()



# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R, 2B):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

liczba = '18E'

kolor = liczba[-1]
numer = int(liczba[0:2])

if kolor == 'R':
    print("Czerwona")
elif kolor == 'C':
    print("Czarna")
else:
    print("Kolor nieznany")

if numer <18:
    print('Mala')
else:
    print('Duza')

if numer % 2 == 0:
    print("Parzysta")
else:
    print('niepatzysta')

# 7. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

temp = '67.544F'

typ = temp[-1]
stopnie = float(temp[:-1])

if typ == 'C':
    temp_kon = stopnie * (9 / 5) + 32
    print(f"Temperatura {temp} to {temp_kon}F.")
elif typ == 'F':
    temp_kon = (stopnie - 32) * (5 /9)
    print(f"Temperatura {temp} to {temp_kon}C.")
else:
    print(f'Podano niepoprawna temperature.')

# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

a = 5
b = 5
c = 5

if a < b + c and b < a + c and c < a + b:
    print('Uda sie narysowac trojkat.')
    if a == b and b == c:
        print('Trojkat rownoboczny')
    elif a == b or a == c or b == c:
        print('Trojkat rownoramienny')
    else:
        print('Trojkąt rożnoboczny')
else:
    print('Nie można narysowac trojkata')
