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
            headers = 'Rose_name Category Url Price Colour Family Fragrance_Strength Flowering Notes Color2 Height Height_Spread'
            bytes_headers = bytes(headers, 'utf-8')
            w.writerow(headers.split())

            source = requests.get(self.url_name).text

            # Parsing in BeautifulSoup

            soup = BeautifulSoup(source, 'lxml')

            # Getting first rose
            # No iteration just yet. The goal is to check that we are getting data for one item.

            for rose in soup.find_all("li", {"class":"item last"}):
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
                color = self.rose_color


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

                # Geting data from the dictionary
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
                height_spread = results.get('Height & Spread:')
                print(height_spread)


                # Printing data to csv file
                # Had to change encoding of name as it was not in utf-8
                w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,category,(price.encode('ascii','ignore')).decode('utf-8'),color,family,fragrance,flowering,notes,color2,height,height_spread])

white = Color('DA_white_class_full.csv', 'https://www.davidaustinroses.co.uk/colour-white-+-cream-show-all', 'white')
red = Color('DA_red_class_full.csv', 'https://www.davidaustinroses.co.uk/colour/red-show-all', 'red')
pink = Color('DA_pink_class_full.csv', 'https://www.davidaustinroses.co.uk/colour/pink-show-all', 'pink')
orange = Color('DA_orange_class_full.csv', 'https://www.davidaustinroses.co.uk/colour-apricot-+-orange-show-all', 'orange')
yellow = Color('DA_yellow_class_full.csv', 'https://www.davidaustinroses.co.uk/colour-yellow-show-all', 'yellow')
purple = Color('DA_purple_class_full.csv', 'https://www.davidaustinroses.co.uk/colour-purple-show-all', 'purple')
bi = Color('DA_bi_class_full.csv', 'https://www.davidaustinroses.co.uk/colour-striped-+-bi-colour-show-all', 'bi colored')
