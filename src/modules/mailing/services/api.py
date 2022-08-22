import requests
import json

from automailing.settings import API_TOKEN


def send_message(phone, text):
    url = 'https://probe.fbrq.cloud/docs#/send/sendMsg'

    headers = {
        "accept" : "application/json",
        "Authorization": API_TOKEN
    }
    parameters = {
        "id": 1,
        "phone": int(phone),
        "text": text
    }

    response = requests.get(url, headers=headers, data=json.dumps(parameters))

    print(response.status_code)

    return response.status_code