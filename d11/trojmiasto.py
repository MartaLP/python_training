import requests

strona = 'https://trojmiasto.pl/'

response = requests.get(strona)
print(response.status_code)
response.raise_for_status()
# print(response.text)

with open('trojmiasto.html', 'w') as plik:
    plik.write(response.text)
    print('zapisałem stronę')
