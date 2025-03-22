import datetime
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()
notification_manager = NotificationManager()

# Search for IATA codes
flight_search = FlightSearch()
sheet_data = data_manager.raw_data["prices"]

# Update IATA codes in sheet
for city in sheet_data:
    flight_search.search_by_location(city['city'], "en-US", "airport", True)
    data_manager.update_iata_data(id=city['id'], iata=flight_search.raw_location_data['locations'][0]['id'])

departure_city = "BOM"
flight_type = "round"
currency = "INR"

for city in sheet_data:
    flight_data = FlightData()
    flight_data.departure_city = departure_city
    flight_data.destination_city = city['iataCode']
    flight_data.date_from = (datetime.datetime.now() + datetime.timedelta(days=1.0)).strftime("%d/%m/%Y")
    flight_data.date_to = (datetime.datetime.now() + datetime.timedelta(days=6.0*30)).strftime("%d/%m/%Y")
    flight_data.nights_in_dst_from = 7
    flight_data.nights_in_dst_to = 28
    flight_data.flight_type = flight_type
    flight_data.currency = currency
    flight_data.price_to = int(city['lowestPrice'])

    flight_search.search_flights(flight_data)

    for flight in flight_search.flight_data['data']:
        message = f"Low price alert! Only {currency} {flight['price']} to fly from" \
                  f" {flight['cityFrom']}-{flight['cityCodeFrom']} to {flight['cityTo']}-{flight['cityCodeTo']} from" \
                  f"{flight_data.date_from} to {flight_data.date_to}."

        notification_manager.send_notification(message=message)






