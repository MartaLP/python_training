from kod.d8.pies import Pies

# tworzę instancje
reksio = Pies('Kiler', 'bokser', 7)
print(reksio)
print(reksio.name)
print(reksio.age)

# instancje posiadają takie same atrybuty
# ale wartości w polach są indywidualne!
burek = Pies('burek', 'mieszaniec', 3)
print(burek.name)
print(burek.age)

reksio.szczeknij(4)
burek.szczeknij(7)

reksio.nakarmij()
print(reksio.hungry)
print(burek.hungry)

burek.hungry = "nie"
print(burek.hungry)

print(burek)