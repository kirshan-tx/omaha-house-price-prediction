import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import random
from get_data import *
import pandas as pd

headers  = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ms;q=0.6,zh-TW;q=0.5,pt;q=0.4",
    "accept-encoding": "gzip, deflate, br",
    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
data = []

def fetch(url):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return response


def parse(response):
    content = BeautifulSoup(response.text, "lxml")
    container = content.find_all("li", class_="jsx-2423110403 component_property-card")

    for listing in container:
        data.append(
            {
                'price': get_price(listing),
                'beds': get_beds(listing),
                'baths': get_baths(listing),
                'sqft': get_sqft(listing),
                'sqftlot': get_sqftlot(listing),
                'broker': get_broker(listing),
                'address': get_address(listing)
            }
        )


def run(pages=1):
    url = "https://www.realtor.com/realestateandhomes-search/Omaha_NE/type-single-family-home,multi-family-home,condo,townhome/nc-hide/fc-hide/"

    for i in range(1,pages+1):
        res = fetch(url + '/pg-' + str(i))
        parse(res)
        time.sleep(random.randint(3, 5))

run(55)
df = pd.DataFrame(data)
df.to_csv('omaha_house_price.csv', index=False)