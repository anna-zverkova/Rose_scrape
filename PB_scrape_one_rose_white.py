import urllib.request
from bs4 import BeautifulSoup
import requests
import csv

# Creating csv

filename = "PB_white.csv"


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_name Url Price Colour Family Fragrance Flowering Color2 Date Height_spread Bsize Btype Suitable'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())

    source = requests.get('https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=12').text

    # Parsing in BeautifulSoup

    soup = BeautifulSoup(source, 'lxml')

    # Getting first rose
    # No iteration just yet. The goal is to check that we are getting data for one item.

    rose = soup.find("li", {"class":"item last pbr-productList-imageContainer"})

    print(rose.prettify())
    rose_item = rose.find("h2", {"class":"product-name"}).a

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
        price = rose.find("p", {"class":"minimal-price"}).text
    except Exception as e:
        price = 'None'
    color = 'white'


# Printing rose data in Terminal
    print(name)
    print(url)
    print(price)
    print(color)


# Scraping from associated page

    linked_page = url

    class AppURLopener(urllib.request.FancyURLopener):
      version = "Mozilla/5.0"

    opener = AppURLopener()
    response2 = opener.open(linked_page)

    page2_soup = BeautifulSoup(response2, 'lxml')

    rose2 = page2_soup.find("div", {"class":"panel-body"})

    print(rose2.prettify())

# Getting extra data from scraped url and adding it to dictionary


    results = {}
    for item in rose2.find_all(class_='row')[0].find_all("div"):
        try:
            characteristic = item.label.string
        except Exception as e:
            characteristic = 'None'
        try:
            type = item.find("div", {"class":"form-control-static"}).text
        except Exception as e:
            type = 'None'
        results[characteristic] = type
        print('Characteristic : {}'.format(characteristic), 'Type : {}'.format(type))

    # Geting data from the dictionary
    family = results.get('Rose Family').strip()
    print(family)
    fragrance = results.get('Fragrance').strip()
    print(fragrance)
    flowering = results.get('Flowering Period').strip()
    print(flowering)
    color2 = results.get('Rose Colour').strip()
    print(color2)
    date = results.get('Date of Introduction').strip()
    print(date)
    height_spread = results.get('Height & Width Range').strip()
    print(height_spread)
    bsize = results.get('Bloom Size').strip()
    print(bsize)
    btype = results.get('Bloom Type').strip()
    print(btype)
    suitable = results.get('Suitable for...').strip()
    print(suitable)

    # Printing data to csv file
    # Had to change encoding of name as it was not in utf-8

    w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,(price.encode('ascii','ignore')).decode('utf-8'),color,family,fragrance,flowering,color2,date,height_spread,bsize,btype,suitable])
