import requests


class DataManager:
    SHEETY_URL_READ_DATA = "https://api.sheety.co/ba68166c9076ef6635473c09d54a2959/flightDeals/prices"

    def __init__(self):
        self.raw_data = self.read_data()

    def read_data(self):
        response = requests.get(url=self.SHEETY_URL_READ_DATA)
        response.raise_for_status()
        return response.json()

    def update_iata_data(self, id, iata):
        parameters = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(url=f"{self.SHEETY_URL_READ_DATA}/{id}", json=parameters)
        response.raise_for_status()