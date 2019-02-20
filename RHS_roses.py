import urllib.request
from bs4 import BeautifulSoup
import requests
import csv
import re

# Creating csv

filename = "RHS_roses.csv"


with open(filename,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    headers = 'Rose_table_data'
    bytes_headers = bytes(headers, 'utf-8')
    w.writerow(headers.split())

    for page_no in range(1,319):
        print(page_no)
        pages = 'http://apps.rhs.org.uk/horticulturaldatabase/summary2.asp?crit=rose&page=' + str(page_no)
        source = requests.get(pages).text
        print(source)
        soup = BeautifulSoup(source, 'lxml')


        table = soup.find("table", { "class" : "mcl results fifty50" })
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            print(cells)
            print(len(cells))

            if len(cells) == 2:
                cell = cells
            else:
                cell = ''

            # Printing data to csv file

            w.writerow([cell])
