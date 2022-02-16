#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

global href

def main_spider():
    global href

    url = input("Enter URL: ")
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)
    
    for link in soup.findAll('a'):
        gep_link = link.get('href')
        print(gep_link) 

    print("\n \n")
    print("\n")
main_spider()
