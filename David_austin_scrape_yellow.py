from bs4 import BeautifulSoup
import requests
import csv

# Creating csv

filename = "David_austin_roses_yellow.csv"


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_name Category Url Price Colour'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())

# Getting website

    source = requests.get('https://www.davidaustinroses.co.uk/colour/yellow-show-all').text

# Parsing in BeautifulSoup

    soup = BeautifulSoup(source, 'lxml', fromEncoding='utf-8')

# Looping through Roses

    for rose in soup.find_all("li", {"class":"item last"}):

        print(rose.prettify())

        rose_item = rose.find("div", {"class":"product-info"}).a

        # Getting data for each rose
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
        color = 'yellow'

        # Printing each rose data in Terminal
        print(name)
        print(url)
        print(category)
        print(price)
        print(color)

        # Printing data to csv file
        # Had to change encoding of name as it was not in utf-8
        w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,category,(price.encode('ascii','ignore')).decode('utf-8'),color])
