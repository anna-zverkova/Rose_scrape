import urllib.request
from bs4 import BeautifulSoup
import requests
import csv

# Creating csv

filename = "DA_white.csv"


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_name Category Url Price Colour Family Fragrance_Strength Flowering Notes Color2 Height'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())

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


# Printing rose data in Terminal
    print(name)
    print(url)
    print(category)
    print(price)
    print(color)

# Scraping from associated page

    linked_page = url

    class AppURLopener(urllib.request.FancyURLopener):
      version = "Mozilla/5.0"

    opener = AppURLopener()
    response2 = opener.open(linked_page)

    page2_soup = BeautifulSoup(response2, 'lxml')

    rose2 = page2_soup.find("li", {"class":"characteristics"})

    print(rose2.prettify())

# Getting extra data from scraped url and adding it to dictionary

    results = {}
    for item in rose2.find_all(class_='characteristics-wrapper')[0].find_all("li"):
        try:
            characteristic = item.h4.text
        except Exception as e:
            characteristic = 'None'
        try:
            type = item.p.text
        except Exception as e:
            type = 'None'
        results[characteristic] = type
        print('Characteristic : {}'.format(characteristic), 'Type : {}'.format(type))
        print(results)

# Printing data to csv file
# Had to change encoding of name as it was not in utf-8
    family = results.get('Family:')
    print(family)
    fragrance = results.get('Fragrance Strength:')
    print(fragrance)
    flowering = results.get('Flowering:')
    print(flowering)
    notes = results.get('Fragrance Notes:')
    print(notes)
    color2 = results.get('Colour:')
    print(color2)
    height = results.get('Height:')
    print(height)

    w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,category,(price.encode('ascii','ignore')).decode('utf-8'),color,family,fragrance,flowering,notes,color2,height])
