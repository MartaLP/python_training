# stworzyć funkcję, która po otrzymaniu liczby
# całkowitej do 1 miliona zwróci wartość True jeśli ta
# liczba jest pierwsza


def czy_pierwsza(x):
    if x > 1000000:
        print("Podana liczba jest większa niz 1000000.")
    else:
        if x <= 2:
            print(f'Liczba {x} jest liczba pierwsza.')
        else:
            pierwsza = True
            for i in range(2, x):
                if x % i == 0:
                    pierwsza=False
                    print(f"Liczba {x} nie jest liczba pierwszą.")
                    break
            if pierwsza == True:
                print(f"Liczba {x} jest liczba pierwszą.")
czy_pierwsza(6)