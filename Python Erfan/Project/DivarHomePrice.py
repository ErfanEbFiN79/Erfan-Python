# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 21:04:35 2025

@author: ebfin
"""

import requests
import re
import pyshorteners
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


page = 1


def persian_to_english(text):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    return text.translate(str.maketrans(persian_digits, english_digits))

def SendRequest(city):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        if len(city) >= 3:
            r = requests.get(f"https://divar.ir/s/kerman/buy-apartment",headers=headers)
        else:
            r = requests.get("https://www.divar.ir")
        return r
    except Exception:
        print("You need connect to the vpn")
def GetData(city):
    request = SendRequest(city)
    b4 = BeautifulSoup(request.text, "html.parser")
    find = b4.find_all("article", class_="kt-post-card kt-post-card--outlined")
    dic = {}
    for home in tqdm(find):
        link_tag = home.find("a", class_="kt-post-card__action")
        if not link_tag or not link_tag.has_attr("href"):
            continue
        
        link = "https://divar.ir" + link_tag["href"]
        title_div = home.find("div", class_="kt-post-card__body")
        title = title_div.get_text(strip=True) if title_div else "بدون عنوان"
        dic[title] = link
    print("We get links")
    return dic
    
def GetDeepData(listOfLink):
    for i in tqdm(listOfLink):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        r = requests.get(i, headers=headers)
        b4 = BeautifulSoup(r.text, "html.parser")
        trs = b4.find_all("tr", class_="kt-group-row__data-row")

        if not trs:
            print("❌ اطلاعات پیدا نشد:", i)
            trs = b4.find_all(".kt-group-row__data-row")
            if not trs:
                print("❌ ")
            else:
                for row in trs:
                    tds = row.find_all("td")
                    values = [td.get_text(strip=True) for td in tds]
                    print("✅", values)
        else:
            for row in trs:
                tds = row.find_all("td")
                values = [td.get_text(strip=True) for td in tds]
                print("✅", values)
        
        time.sleep(2)
        
#city = input("Enter name of city: ")
r = GetData('kerman')
print(r.values())
GetDeepData(r.values())