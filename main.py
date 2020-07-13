import csv
import requests
import urllib3
import urllib.parse
from googlesearch import search
from bs4 import BeautifulSoup
from scrape_result import (
    get_description,
    get_site_name
)

rank = 0

urllib3.disable_warnings()

if __name__ == '__main__':
    
    keyword = input("Please input your keyword: ") 
    no = int(input("How many outputs you want to be created: "))

    filename = keyword + ".csv"
    writer = open(filename, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(writer, delimiter=";")

    for url in search(keyword, stop=no):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        rank = rank + 1
        req = requests.get(url, verify=False, headers=headers)
        if req.status_code == 200:

            
            url_unparse = urllib.parse.unquote(url)
            html = BeautifulSoup(req.content, 'html.parser')
            csv_writer.writerow([rank, url_unparse,  get_site_name(html, url), get_description(html)])
            print('adding data on csv')
    writer.close()
print("Done")