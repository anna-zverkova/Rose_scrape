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
            headers = 'Rose_name Category Url Price Colour'
            bytes_headers = bytes(headers, 'utf-8')
            w.writerow(headers.split())

        # Getting website

            source = requests.get(self.url_name).text

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
                color = self.rose_color

                # Printing each rose data in Terminal
                print(name)
                print(url)
                print(category)
                print(price)
                print(color)

                # Printing data to csv file
                # Had to change encoding of name as it was not in utf-8
                w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,category,(price.encode('ascii','ignore')).decode('utf-8'),color])

red = Color('DA_red_class.csv', 'https://www.davidaustinroses.co.uk/colour/red-show-all', 'red')
pink = Color('DA_pink_class.csv', 'https://www.davidaustinroses.co.uk/colour/pink-show-all', 'pink')
orange = Color('DA_orange_class.csv', 'https://www.davidaustinroses.co.uk/colour-apricot-+-orange-show-all', 'orange')
yellow = Color('DA_yellow_class.csv', 'https://www.davidaustinroses.co.uk/colour-yellow-show-all', 'yellow')
white = Color('DA_white_class.csv', 'https://www.davidaustinroses.co.uk/colour-white-+-cream-show-all', 'white')
purple = Color('DA_purple_class.csv', 'https://www.davidaustinroses.co.uk/colour-purple-show-all', 'purple')
bi = Color('DA_bi_class.csv', 'https://www.davidaustinroses.co.uk/colour-striped-+-bi-colour-show-all', 'bi colored')
