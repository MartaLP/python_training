
# zmienna na poziomie globalnym
imie = "Ola"

def zmien_imie():
    # deklarujemy, że wew. funkcji będziemy
    # używać zmiennej globalnej
    global imie
    imie = 'Ala'    # zmiana wartości zmiennej globalnej


zmien_imie()
print(imie)

# należy uważać ze zmiennymi globalnymi
# funkcje, które działają na zmiennych globalnych
# mogą je zmieniać czasami "niejawnie"
# wprowadzając nieoczekiwane dane