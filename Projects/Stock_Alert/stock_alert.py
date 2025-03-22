import requests
import datetime
import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCKS = ""
API_KEY_NEWS = ""

parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": API_KEY_STOCKS,
}

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response.raise_for_status()
raw_stock_data = response.json()
today = datetime.datetime.today().date()
yesterday = today - datetime.timedelta(days=1.0)
stock_price_yesterday = float(raw_stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])

# - Get the day before yesterday's closing stock price
day_before_yesterday = yesterday - datetime.timedelta(days=1.0)
stock_price_day_before_yesterday = float(raw_stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint:
# https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(stock_price_yesterday - stock_price_day_before_yesterday)

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
percentage_difference = (difference / stock_price_yesterday) * 100
print(percentage_difference)

# Fetch latest news about the company if percentage difference is greater than 5%

if int(percentage_difference) > 0:
    parameters_news = {
        "q": COMPANY_NAME,
        "from": str(day_before_yesterday),
        "sortBy": "popularity",
        "language": "en",
        "apiKey": API_KEY_NEWS,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    response.raise_for_status()

    raw_news_feed = response.json()

# Create a new list of the first 3 article's headline and description using list comprehension.
    news_feed = raw_news_feed["articles"][0:4:1]

# Send each article as a separate message via Twilio.
    for news in news_feed:
        text_message: str
        if stock_price_yesterday > stock_price_day_before_yesterday:
            text_message = f"TSLA: 🔺{percentage_difference}%\nHeadline:{news['title']}\nBrief:{news['description']}"
        else:
            text_message = f"TSLA: 🔻{percentage_difference}%\nHeadline:{news['title']}\nBrief:{news['description']}"
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"{text_message}",
            from_="+16204078395",
            to="+917719997333"
        )
        print(message.status)








