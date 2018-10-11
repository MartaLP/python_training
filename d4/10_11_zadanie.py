# 11. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

lista = []

for i in range(100):
    if i <= 1:
        lista.append(i)
    else:
        lista.append(lista[i - 1] + lista[i - 2])

print(lista)