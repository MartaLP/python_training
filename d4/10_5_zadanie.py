# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

i = 0
while i < len(lista_b):
    if lista_b.count(lista_b[i])>1:
        lista_b.remove((lista_b[i]))
    i += 1
print(lista_b)