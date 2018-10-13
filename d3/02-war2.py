# funkcja input pobiera stringa od usera
nazwisko = input("Podaj nazwisko:\n ")

# wszystko co wpisuje użytkownik jest stringiem
print(type(nazwisko))

# usunąć whitespace'y z początku i końca
nazwisko = nazwisko.strip()

# jeśli w stringu są cyfry, napisać komunikat
# i przerwać program
if not nazwisko.isalpha():
    print("Muszą być tylko litery")
    exit(99)

# nazwisko = nazwisko.strip()
# zamienić wszystkie litery na duże
naz_czyste = nazwisko.upper()

print(naz_czyste)

if naz_czyste[-1] == "A":
    print("Chyba jesteś kobietą.")
elif naz_czyste.endswith("SKI"):
    print("Najprawdopodobniej jesteś mężczyzną.")
else:
    print("Nie wiem", end="\n¯\\\\\\_(ツ)\_/¯\n")



print("Koniec programu")
