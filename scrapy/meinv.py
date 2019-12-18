import requests
from bs4 import BeautifulSoup
import os 


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding 
        return r.text
    except:
        return ""

def prassHTML(html, addresses):
    soup = BeautifulSoup(html, "html.parser")
    for address in soup.find_all('img'):
        addresses.append(address['data-original'])


def saveIMAGE(addresses):    
    root = "/home/harden/python-practice/scrapy/"
    for url in addresses:
        path = root + url.split('/')[-1]
        url = url.split(' ')[0]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("Picture Save")
            else:
                print("Path exists")
        except:
            print("False")



list_address = []
url = "https://www.82maokk.com/arthtml/9597.html"
html = getHTMLText(url)
prassHTML(html, list_address)
saveIMAGE(list_address)

