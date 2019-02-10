import urllib.request
from bs4 import BeautifulSoup
import requests
import csv
import re

# Creating csv

filename = "Harkness_all_bush_roses.csv"


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_name Url Price Type Name2 Rating_Scent Flower Flowers_per_Cluster Height Text Registered_Name'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())

    for page_no in range(1,6):
        print(page_no)
        pages = 'https://www.roses.co.uk/this-is-the-br/bush-roses-bare-root?page=' + str(page_no)
        source = requests.get(pages).text
        print(source)
        soup = BeautifulSoup(source, 'lxml')

        for rose in soup.find_all("div", {"class":"product-box col-xs-6 col-sm-4 gallery"}):
            print(rose.prettify())
            rose_item = rose.find("div", {"class":"product-title box-shadow-container box-shadow"})
            print("rose_item")

            try:
                pre_url = rose.find(href=True)
            except Exception as e:
                pre_url = 'None'
            try:
                url =  re.findall(r'href=[\'"]?([^\'" >]+)', str(pre_url))
            except Exception as e:
                url = 'None'
            try:
                name = rose.find('h5').text
            except Exception as e:
                name = 'None'
            try:
                price = rose_item.find("span", {"class":"price"}).text
            except Exception as e:
                price = 'None'
            _type_ = 'Bush Roses (Bare Root)'


        # Printing rose data in Terminal
            print(name)
            print(url[0])
            print(price)
            print(_type_)

            # Scraping from associated page

            linked_page = url[0]

            class AppURLopener(urllib.request.FancyURLopener):
                version = "Mozilla/5.0"

            opener = AppURLopener()
            response2 = opener.open(linked_page)

            page2_soup = BeautifulSoup(response2, 'lxml')

            rose2 = page2_soup.find("div", {"class":"reviews-hidden"})

            print(rose2.prettify())

            # Getting extra data from scraped url and adding it to dictionary

            element = 0
            results = {}
            for item in rose2.find_all("p"):
                try:
                    element += 1
                except Exception as e:
                    element = 'None'
                try:
                    rose_info = item.span.string
                except Exception as e:
                    rose_info = 'None'
                results[element] = rose_info
                print('Element : {}'.format(element), 'Rose_type : {}'.format(rose_info))

            # print(results)
            # Geting data from the dictionary
            name2 = results.get(1)
            print(name2)
            rating_scent = results.get(2)
            print(rating_scent)
            flower =results.get(3)
            print(flower)
            cluster = results.get(4)
            print(cluster)
            height = results.get(5)
            print(cluster)
            text = results.get(6)
            print(text)
            reg_name = results.get(7)
            print(reg_name)



            # Printing data to csv file
            # Had to change encoding of name as it was not in utf-8

            w.writerow([(name.encode('ascii','ignore')).decode('utf-8'), \
                        linked_page, \
                        (price.encode('ascii','ignore')).decode('utf-8'), \
                        _type_, \
                        (str(name2).encode('ascii','ignore')).decode('utf-8'), \
                        (str(rating_scent).encode('ascii','ignore')).decode('utf-8'), \
                        (str(flower).encode('ascii','ignore')).decode('utf-8'), \
                        (str(cluster).encode('ascii','ignore')).decode('utf-8'), \
                        (str(height).encode('ascii','ignore')).decode('utf-8'), \
                        (str(text).encode('ascii','ignore')).decode('utf-8'), \
                        (str(reg_name).encode('ascii', 'ignore')).decode('utf-8')])
