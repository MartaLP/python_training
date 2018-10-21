from pprint import pprint

nabial = ['mleko', 'ser', 'masło']
chemia = ['cif', 'ajax', 'ludwik']

# tworzymy listę zawierającą dwie listy
paz = [nabial, chemia]

# tworzymy kopie listy paz
# wszystkie trzy sposoby tworzą płytką kopię
lis = paz.copy()
gru = paz[:]
sty = list(paz)

pprint(f"paź: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")
pprint(f"sty: {sty}")

# dodajemy produkt do wewnętznej listy
# październikowej
paz[0].append('jogurt')

# okazuje się, że wszystkie listy mają
# dopisany produkt
# jest to spowodowane wykonaniem płytkiej kopii
# jeśli zawarty w liście jest typ złożony (inna lista)
# to w czasie kopiowania, kopiowany jest adres pamięci
# a nie wartości w tej liście
pprint(f"paź: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")
pprint(f"sty: {sty}")
