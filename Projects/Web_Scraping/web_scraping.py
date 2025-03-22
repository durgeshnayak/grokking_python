import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import requests

URL = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"
r = requests.get(url=URL)

html_data = r.text

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

soup = BeautifulSoup(markup=html_data, features="html.parser")

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    if len(col) > 0:
        data = data.append({"Name": col[1].text.strip(), "Market Cap (US$ Billion)": col[2].text.strip()}, ignore_index=True)

print(data.head())

data.to_json(path_or_buf="./bank_market_cap.json")






