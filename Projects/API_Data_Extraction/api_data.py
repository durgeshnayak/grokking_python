import requests
import pandas
import json

URL = "https://api.apilayer.com/exchangerates_data/latest"

payload = {"base": "EUR"}
# Update value for apikey in below dictionary
headers = {"apikey": ""}
r = requests.get(url=URL, headers=headers, params=payload)

json_object = json.dumps(r.json()["rates"])

with open(file="./data.json", mode="w") as file_stream:
    file_stream.write(json_object)

df = pandas.read_json(path_or_buf="./data.json", typ="series")

df.to_csv(path_or_buf="./exchange_rates_1.csv", header=["Rates"])
