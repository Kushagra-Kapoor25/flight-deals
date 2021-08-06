import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_alert(self, message):
        message = self.client.messages.create(
            body=message,
            from_=f"whatsapp:{TWILIO_VIRTUAL_NUMBER}",
            to=f"whatsapp:{TWILIO_VERIFIED_NUMBER}",
        )
        print(message.status)