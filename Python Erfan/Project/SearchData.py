import requests
import re
import pyshorteners
from bs4 import BeautifulSoup
from tqdm import tqdm

def shorten_url(long_url):
    """
    Shortens a given long URL using TinyURL.
    """
    s = pyshorteners.Shortener(timeout=10)
    try:
        short_url = s.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return long_url

def GetData(url, tag):
    r = Start(url)
    soup = BeautifulSoup(r.text, "html.parser")
    a_href = soup.select(tag)
    dicData = {}
    for item in tqdm(a_href):
        #item = item.encode('utf-8')
        res = re.search(r'href="([^"]+)"', str(item))
        res2 = re.search(r'title="([^"]+)"', str(item))
        if res:
            if res2:
                print(f"{res2.group(0)[:30]} = link {shorten_url(f'{url}{res.group(1)}')}")
                dicData[res2.group(0)] = shorten_url(f"{url}{res.group(1)}")
            else:
                print(f"{item.text[0:30]} = link {shorten_url(f'{url}{res.group(1)}')}")
                dicData[item.text] = shorten_url(f"{url}{res.group(1)}")
        else:
            if res2:
                print(f"{res2.group(0)}")
            else:
                print(f"{item.text}")
def Start(url):
    try:
        r = requests.get(f'{url}')
        return r
    except Exception as e:
        print(f"You need coonect to the vpn")
        exit()
    else:
        print("You are connected to the vpn")
        return True



Data = input("Enter the url: ")
Data = "https://" + Data
tag = input("Enter the tag: ")
print(GetData(Data,tag))
