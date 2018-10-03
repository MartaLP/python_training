# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

lista_a =["abc", "cfd", "gft", "ddd", "dd"]
lista_b =["bbc", "cfd", "TRt","ury"]

wspolny_el=set(lista_b) & set(lista_a)
if len(wspolny_el) > 0:
    print(True)
else:
    print(False)

# inaczej, bez set
if False:
    i = 0
    if len(lista_a) > len(lista_b):
        while i < len(lista_a):
            if lista_a[i] in lista_b:
                print(True)
                break
            i += 1
    else:
        while i < len(lista_b):
            if lista_b[i] in lista_a:
                print(True)
                break
            i += 1

