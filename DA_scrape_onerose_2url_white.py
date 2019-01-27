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
