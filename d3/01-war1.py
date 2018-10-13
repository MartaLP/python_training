# Mała instrukcja warunkowa
if True:
    pass

# Podobnie
if 5 == 10 / 2:
    print("Wnętrze ifa")

# if rozpoczyna instrukcje warunkowe
if 5 != 20 / 4:
    # ta instrukcja będzie wykonana jesli wyrazenie w if-ie bedzie True
    print("Drugi if")
# elif to dodatkowy warunek, sprawdzany jeśli wcześniejszy if/elif był False
elif 5 == 5 and 20 % 2 == 1:
    print("Drugi if, elif")
elif 45 % 3 == 12:
    print("elif modulo")
# else to przypadek ostateczny, wykonywany, gdy wszystkie ify/elify były False
else:
    print("Instrukcja ostateczna")

# ta instrukcja nie należy do bloku if-elif-else bo jest na tym samym
# poziomie co powyższy if
print("Pierwsza instrukcja po if")


imie = "konstantynopolitanczykowianka"

# operator in sprawdza czy element jest w kolekcji
if 'Z' in imie:
    print("jest Z w imieniu!")
else:
    print("Nie ma Z w imieniu")
