import requests
import os
from dotenv import load_dotenv
load_dotenv()


SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
AUTHORIZATION = os.getenv("AUTHORIZATION")

headers = {
    "Authorization": AUTHORIZATION
}


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data_from_sheet(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=headers)
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_sheet_data(self):
        for data in self.sheet_data:
            update_data = {
                "price": {
                    "iataCode": data["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{data['id']}", json=update_data, headers=headers)
            print(response.text)
