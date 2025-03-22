import requests
import lxml
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.in/Logitech-Advanced-Illuminated-Bluetooth-Responsive/dp/B08196YFMK/"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}

response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(markup=response.text, features="lxml")
price_tag = soup.find_all(name="input", id="priceValue")
item_price = float(price_tag[0]["value"])

