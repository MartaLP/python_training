from pprint import pprint

# moduł copy zawiera funkcje kopiujące
# deepcopy to głęboka kopia
# skopiuje ona wartości nawet z typów złożonych
from copy import deepcopy

nabial = ['mleko', 'ser', 'masło']
chemia = ['cif', 'ajax', 'ludwik']

paz = [nabial, chemia]
lis = deepcopy(paz)
gru = deepcopy(paz)

pprint(f"paź: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")

paz[0].append('jogurt')

# teraz pozostałe miesiące są nie zmienione
pprint(f"paź: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")
