import requests
import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.account_sid = ""
        self.auth_token = ""
        self.client = Client(self.account_sid, self.auth_token)

    def send_notification(self, message):
        txt_message = self.client.messages.create(
            body=message,
            from_="+16204078395",
            to="+917719997333"
        )
