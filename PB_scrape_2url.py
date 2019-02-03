import urllib.request
from bs4 import BeautifulSoup
import requests
import csv

class Color:
    def __init__(self, file_name, url_name, rose_color):
        self.file_name = file_name
        self.url_name = url_name
        self.rose_color = rose_color

        # Creating csv

        with open(self.file_name,'w',newline='',encoding='utf-8') as f:
            w = csv.writer(f)
            headers = 'Rose_name Url Price Colour Family Fragrance Flowering Color2 Date Height_spread Bsize Btype Suitable'
            bytes_headers = bytes(headers, 'utf-8')
            w.writerow(headers.split())

            source = requests.get(self.url_name).text

            # Parsing in BeautifulSoup

            soup = BeautifulSoup(source, 'lxml')

            # Getting first rose
            # No iteration just yet. The goal is to check that we are getting data for one item.
            for rose in soup.find_all("li", {"class":"item last pbr-productList-imageContainer"}):
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
                color = self.rose_color
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


                try:
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
                except Exception as e:
                    print('None')
                # Geting data from the dictionary
                family = results.get('Rose Family')
                print(family)
                fragrance = results.get('Fragrance')
                print(fragrance)
                flowering = results.get('Flowering Period')
                print(flowering)
                color2 = results.get('Rose Colour')
                print(color2)
                date = results.get('Date of Introduction')
                print(date)
                height_spread = results.get('Height & Width Range')
                print(height_spread)
                bsize = results.get('Bloom Size')
                print(bsize)
                btype = results.get('Bloom Type')
                print(btype)
                suitable = results.get('Suitable for...')
                print(suitable)
                # Printing data to csv file
                # Had to change encoding of name as it was not in utf-8
                w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,(price.encode('ascii','ignore')).decode('utf-8'),color,family,fragrance,flowering,color2,date,height_spread,bsize,btype,suitable])

white = Color('PB_white_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=12', 'white')
yellow = Color('PB_yellow_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=17', 'yellow')
orange = Color('PB_orange_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=16', 'orange')
red = Color('PB_red_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=15', 'red')
light_pink = Color('PB_light_pink_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=13', 'light_pink')
dark_pink = Color('PB_dark_pink_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=14', 'dark_pink')
purple = Color('PB_purple_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=18', 'purple')
bi_color = Color('PB_bi_color_full.csv', 'https://www.classicroses.co.uk/roses.html?limit=256&pbr_rose_colour=19', 'bi_color')
