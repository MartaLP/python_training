import requests
import json
from pprint import pprint
from random import randint
from pobieracz import pobierz
from os.path import basename

najnowszy_komiks = 'http://xkcd.com/info.0.json'

odpowiedz = requests.get(najnowszy_komiks)
odpowiedz.raise_for_status()
# pprint(odpowiedz.json())

info = odpowiedz.json()
# pprint(info['num']
maks_komiks = info['num']
nr_losowy = randint(1, maks_komiks)


# adres = 'http://xkcd.com/xxx/info.0.json'.replace('xxx', str(nr_losowy))
adres = 'http://xkcd.com/{}/info.0.json'.format(nr_losowy)
# print(adres)

odp_los = requests.get(adres)
odp_los.raise_for_status()

pprint(odp_los)
pprint(odp_los.json())

link = odp_los.json()['img']

nazwa_pliku = basename(link)
pobierz(link, nazwa_pliku)