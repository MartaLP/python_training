import os

path = "c:\\moj_plik1.txt"

if os.path.exists(path):
    with open(path) as file:
        print(file.read())

else:
    print('Podany plik nie istnieje')

print('Koniec programu')

raise ValueError('błąd')