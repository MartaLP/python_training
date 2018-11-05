import requests
import bs4
import urllib
import os

main_page = 'https://xkcd.com/'
prev = ''
num_pictures = int(input("How many pictures you want to save:\n"))

for i in range (num_pictures):

    page_address = main_page + prev
    response = requests.get(page_address)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    picture = soup.find("div", {"id": "comic"}).find("img").attrs['src']
    urllib.request.urlretrieve('''https:''' + picture, os.path.basename('''https:''' + picture))
    prev = soup.find("ul", {"class": "comicNav"}).find("a", {"rel": "prev"}).attrs["href"]



