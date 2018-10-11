# 4. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
lista_b = []

i = 0
while i < len(lista_a):
    if lista_a[i] not in lista_b:
        lista_b.append(lista_a[i])
    i += 1
print(lista_b)