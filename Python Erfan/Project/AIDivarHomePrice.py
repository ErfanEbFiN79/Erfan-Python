import requests
from bs4 import BeautifulSoup
import csv
import time

def persian_to_english(text):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    return text.translate(str.maketrans(persian_digits, english_digits))

headers = {
    "User-Agent": "Mozilla/5.0"
}

base_url = "https://divar.ir/s/kerman/buy-residential"
page = 1
all_ads = []

while True:
    print(f"📄 صفحه {page} ...")
    url = base_url if page == 1 else f"{base_url}?page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    ads = soup.find_all("article", class_="kt-post-card kt-post-card--outlined")

    if not ads:
        print("✅ پایان صفحات.")
        break

    for ad in ads:
        ad_data = {
            "title": "",
            "link": "",
            "price": "",
            "area": "",
            "rooms": "",
            "year": "",
            "elevator": 0,
            "parking": 0,
            "storage": 0
        }

        link_tag = ad.find("a", class_="kt-post-card__action")
        if not link_tag or not link_tag.has_attr("href"):
            continue

        link = "https://divar.ir" + link_tag["href"]
        ad_data["link"] = link

        title_div = ad.find("div", class_="kt-post-card__body")
        if title_div:
            ad_data["title"] = title_div.get_text(strip=True)

        try:
            ad_response = requests.get(link, headers=headers)
            ad_soup = BeautifulSoup(ad_response.text, "html.parser")

            # قیمت
            price_tag = ad_soup.find("div", string="قیمت")
            if price_tag:
                next_tag = price_tag.find_next()
                if next_tag:
                    ad_data["price"] = persian_to_english(next_tag.get_text(strip=True))

            # مشخصات اصلی: متراژ، ساخت، اتاق
            detail_row = ad_soup.find("tr", class_="kt-group-row__data-row")
            if detail_row:
                tds = detail_row.find_all("td")
                if len(tds) >= 3:
                    ad_data["area"] = persian_to_english(tds[0].get_text(strip=True))
                    ad_data["year"] = persian_to_english(tds[1].get_text(strip=True))
                    ad_data["rooms"] = persian_to_english(tds[2].get_text(strip=True))

            # امکانات: آسانسور، پارکینگ، انباری
            features_table = ad_soup.find("table", class_="kt-group-row")
            if features_table:
                ths = features_table.find_all("th")
                tds = features_table.find_all("td")
                for th, td in zip(ths, tds):
                    label = th.get_text(strip=True)
                    value = td.get_text(strip=True)
                    if label == "آسانسور":
                        ad_data["elevator"] = 1 if "✓" in value else 0
                    elif label == "پارکینگ":
                        ad_data["parking"] = 1 if "✓" in value else 0
                    elif label == "انباری":
                        ad_data["storage"] = 1 if "✓" in value else 0

            all_ads.append(ad_data)
            time.sleep(1.2)

        except Exception as e:
            print(f"❌ خطا در آگهی: {link} | {e}")
            continue

    page += 1
    time.sleep(1.5)

# ذخیره در CSV
with open("divar_kerman_houses.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(all_ads[0].keys()))
    writer.writeheader()
    writer.writerows(all_ads)

print("✅ ذخیره در فایل divar_kerman_houses.csv انجام شد.")
