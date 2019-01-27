import urllib.request
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.davidaustinroses.co.uk/colour-white-+-cream').text

# Parsing in BeautifulSoup

soup = BeautifulSoup(source, 'lxml')

# Getting first rose
# No iteration just yet. The goal is to check that we are getting data for one item.

rose = soup.find("li", {"class":"item last"})

print(rose.prettify())
rose_item = rose.find("div", {"class":"product-info"}).a

# Getting data for the first rose
try:
    name = rose_item.get('title')
except Exception as e:
    name = 'None'
try:
    url = rose_item.get('href')
except Exception as e:
    url = 'None'
try:
    category = rose.find("div", {"class":"category"}).text
except Exception as e:
    category = 'None'
try:
    price = rose.find("div", {"class":"price-box"}).span.text
except Exception as e:
    price = 'None'
color = 'white'


# Printing each rose data in Terminal
print(name)
print(url)
print(category)
print(price)
print(color)

# scraping from accosiated pages

linked_page = url

class AppURLopener(urllib.request.FancyURLopener):
  version = "Mozilla/5.0"

opener = AppURLopener()
response2 = opener.open(linked_page)

page2_soup = BeautifulSoup(response2, 'lxml')

rose2 = page2_soup.find("li", {"class":"characteristics"})

print(rose2.prettify())

# getting extra data from scraped url


for item in rose2.find_all(class_='characteristics-wrapper')[0].find_all("li"):
    try:
        characteristic = item.h4.text
    except Exception as e:
        characteristic = 'None'
    try:
        type = item.p.text
    except Exception as e:
        type = 'None'
    print('Characteristic : {}'.format(characteristic), 'Type : {}'.format(type))
