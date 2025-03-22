import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)

parameters = {
    "lat": float(latitude),
    "lng": float(longitude),
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(f"Sunrise Hour: {data['results']['sunrise'].split('T')[1].split(':')[0]}")
print(f"Sunset Hour: {data['results']['sunset'].split('T')[1].split(':')[0]}")
