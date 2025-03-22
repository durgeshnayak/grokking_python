import requests
import os
from twilio.rest import Client

API_KEY = ""

parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
forecast_data = weather_data["list"]

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

for forecast in forecast_data:
    if int(forecast["weather"][0]["id"]) != 800:
        message = client.messages.create(
            body=f"{forecast['weather'][0]['description']} expected at {forecast['dt_txt']}",
            from_="+16204078395",
            to="+917719997333"
        )
        print(message.status)




