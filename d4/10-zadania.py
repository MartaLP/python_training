### Listy
# 1. napisz program sumujący wszystkie elementy w liscie
lista = [2, 5, 7, 8]

suma = 0
for element in lista:
    suma += element
print(sum)

# 2. znajdz najwiekszy / najmniejszy element w liscie

lista = [700, -5, 20, 4567, 7, 17, -800]

najwiekszy = max(lista)
najmniejszy = min(lista)

print(f'Najmniejszt: {najmniejszy}, najwiekszy: {najwiekszy}')

# 3. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

slowa = ["lol", "kaboom", "foo", "kajak"]

liczba = 0
for element in slowa:
    if element[0] == element[-1]:
        liczba += 1
print(liczba)

# 4. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]

lista_b = []

for element in lista_a:
    if lista_a.count(element) == 1:
        lista_b.append(element)
print(lista_b)

# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

for element in lista_b:
    if lista_b.count(element) > 1:
        lista_b.remove(element)

print(lista_b)

# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
lista_a = [1, 2, 44]
lista_b = [11, 2, 414]

for element in lista_a:
    if element in lista_b:
        print(f'Conajmniej jeden wspolny element: {element}')
        break


### Pętle

# 7. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1
#    cena, zaplacono, reszta
cena = 2.75
zaplacono = 102
wartosci = [5, 2, 1, 0.5, 0.2, 0.1]

do_wydania = zaplacono - cena
print(f'Do wydania: {do_wydania}.')

reszta = []

for wartosc in wartosci:
    if do_wydania // wartosc > 0:
        i=0
        while i < int(do_wydania // wartosc):
            reszta.append(wartosc)
            i += 1
        do_wydania = round(do_wydania - (wartosc * (do_wydania // wartosc)), 2)
print(f'Reszta: {reszta}')


# 8. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
#

wysokosc = 4

for i in range(wysokosc):
    print(' ' * (wysokosc - i - 1) + '#' * (i * 2 + 1))

# 9. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie
zakres = range(3)
parzyste = 0
nieparzyste = 0

for i in zakres:
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Ilosc liczb parzystych: {parzyste}, ilosc liczb nieparzysty: {nieparzyste}.')

# 10. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

for i in range(21):
    if i % 4 != 0:
        print(i)



# 11. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
fib =[]

for i in range(101):
    if i < 2:
        fib.append(i)
    else:
        fib.append(fib[i-2] + fib[i-1])

print(f'Ciag Fibonacciego: {fib}')

# 12. oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

wiek_psa_ludzki = 15
psi_wiek = []

if wiek_psa_ludzki > 2:
    psi_wiek.append(2)
    psi_wiek.append(wiek_psa_ludzki-2)
else:
    psi_wiek.append(wiek_psa_ludzki)
    psi_wiek.append(0)

wiek_psa_psi = 10.5 * psi_wiek[0] + 4 * psi_wiek[1]
print(wiek_psa_psi)
