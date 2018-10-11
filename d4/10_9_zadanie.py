# 9. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

zakres=range(11)
parz, nieparz = 0, 0

for i in zakres:
    if i % 2 == 0:
        parz += 1
    else:
        nieparz += 1
print("Zakres: {} \nIlosc liczb parzystych: {},\nIlosc nieparzystych: {}".format(zakres, parz, nieparz))

