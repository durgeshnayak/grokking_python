import requests
from flight_data import FlightData


class FlightSearch:
    TEQUILA_URL_LOCATIONS_QUERY = "https://api.tequila.kiwi.com/locations/query"
    TEQUILA_URL_SEARCH_QUERY = "https://api.tequila.kiwi.com/v2/search"
    API_KEY = ""

    def __init__(self):
        self.raw_location_data = None
        self.flight_data = None

    def search_by_location(self, city, locale, location_types, active_only):
        headers = {
            "apikey": self.API_KEY,
        }

        parameters = {
            "term": city,
            "locale": locale,
            "location_types": location_types,
            "active_only": active_only,
        }

        response = requests.get(url=self.TEQUILA_URL_LOCATIONS_QUERY, params=parameters, headers=headers)
        response.raise_for_status()
        self.raw_location_data = response.json()

    def search_flights(self, flight_details: FlightData):
        headers = {
            "apikey": self.API_KEY,
        }

        parameters = {
            "fly_from": flight_details.departure_city,
            "fly_to": flight_details.destination_city,
            "date_from": flight_details.date_from,
            "date_to": flight_details.date_to,
            "nights_in_dst_from": flight_details.nights_in_dst_from,
            "nights_in_dst_to": flight_details.nights_in_dst_to,
            "flight_type": flight_details.flight_type,
            "curr": flight_details.currency,
            "price_to": flight_details.price_to,
        }

        response = requests.get(url=self.TEQUILA_URL_SEARCH_QUERY, params=parameters, headers=headers)
        response.raise_for_status()
        self.flight_data = response.json()
