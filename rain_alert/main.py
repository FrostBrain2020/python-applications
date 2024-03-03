import os
import requests
from twilio.rest import Client
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
own_api_key = os.environ["OWN_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
phone = "+48..."

parameters = {
    "q": "Lodz,PL",
    "cnt": 4,
    "appid": own_api_key,
}


def will_rain(daily_weather):
    ''' Input: weather list for the next 12 hours divided into 3-hour slots
        Output: Boolean condition based on value of id from https://openweathermap.org/weather-conditions'''
    for every_3_hours in daily_weather:
        condition_code = every_3_hours['weather'][0]['id']
        if condition_code < 700:
            return True
        else:
            return False


response = requests.get(OWM_ENDPOINT, parameters)
response.raise_for_status()
weather_data = response.json()['list']
if will_rain(weather_data):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+13513005694",
        to=phone
    )
    print(message.status)