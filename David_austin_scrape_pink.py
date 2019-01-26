from bs4 import BeautifulSoup
import requests
import csv

# Creates csv


filename = "David_austin_roses_pink_2.csv"
# csv_writer = csv.writer(filename)
# csv_writer.writerow(['Rose_name', 'Category', 'Url', 'Price', 'Colour'])


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_name Category Url Price Colour'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())


    source = requests.get('https://www.davidaustinroses.co.uk/colour/pink-show-all').text

    soup = BeautifulSoup(source, 'lxml', fromEncoding='utf-8')

    # used to get only first rose mentioned on the page
    # rose = soup.find("li", {"class":"item last"})

    for rose in soup.find_all("li", {"class":"item last"}):

        print(rose.prettify())

        rose_item = rose.find("div", {"class":"product-info"}).a

        # print(rose_item)
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
        color = 'pink'

        print(name)
        print(url)
        print(category)
        print(price)
        print(color)

        w.writerow([(name.encode('ascii','ignore')).decode('utf-8'),url,category,price,color])
