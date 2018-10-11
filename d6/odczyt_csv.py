# wyjscie = [
#     ['Jan','Kowalski',34,3000.00],
#     ['Adam','Turek',45,8000.00]
# ]

baza = []

# otwieramy plik
with open('baza.csv', encoding='utf-8') as file:

    # wczytujemy linijka po linijce
    linia = file.readline()

    while linia != '':
    #     # trim na końcu
        linia = linia.rstrip()

    #     # split po przecinku
        osoba = linia.split(',')

    #     # pozycje 2 i 3 odpowienio zmieniamy
        osoba[2] = int(osoba[2])
        osoba[3] = int(osoba[3])
        print(osoba)
        baza.append(osoba)
        linia = file.readline()

print(baza)


