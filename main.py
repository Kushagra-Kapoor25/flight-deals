import os
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from dotenv import load_dotenv
load_dotenv()

ORIGIN_CITY_IATA = os.getenv("ORIGIN_CITY_IATA")

data_manager = DataManager()
sheet_data = data_manager.get_data_from_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.sheet_data = sheet_data
    data_manager.update_sheet_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_alert(
            message=f"Low price alert! ✈️\n"
                    f"Only ₹{flight.price} to fly from *{flight.origin_city}-{flight.origin_airport}* to"
                    f" *{flight.destination_city}-{flight.destination_airport}*, from {flight.out_date} to {flight.return_date}."
        )






