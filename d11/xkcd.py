import requests
import bs4
from pprint import pprint

strona = 'https://xkcd.com/'

response = requests.get(strona)
response.raise_for_status()

# with open('xkcd.html', 'w') as plik:
#     plik.write(response.text)

zupa = bs4.BeautifulSoup(response.text, "html.parser")
# kluska = zupa.select_one('div #comic img')
# kluska = zupa.select('div #comic img')
# pprint(kluska)
# print(kluska['alt'])
# print(kluska['src'])
# print(kluska['title'])

poprzedni = zupa.select('.comicNav li a["rel=prev"]')

for el in poprzedni:
    print(el)

