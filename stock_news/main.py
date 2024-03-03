import requests
import os
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
QUESTION = "+Tesla Inc OR +Musk OR +TSLA"
PRICE_JUMP = 1
NUM_ARTICLES = 3
alphavantage_api_key = os.environ["STOCK_API_KEY"]
news_api_key = os.environ["NEWS_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
phone = "+48..."

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api_key,
}

stock_info = {
    "stock_news": False,
    "trend": None,
    "value": None,
}


def calculate_stock_price():
    global stock_info
    trend = "🔺"
    two_days_ego = yesterday - dt.timedelta(days=1)
    response = requests.get(STOCK_ENDPOINT, stock_params)
    response.raise_for_status()
    yesterday_price = float(response.json()["Time Series (Daily)"][str(yesterday)]["4. close"])
    two_days_ego_price = float(response.json()["Time Series (Daily)"][str(two_days_ego)]["4. close"])
    difference = yesterday_price - two_days_ego_price
    percentage = abs(difference / yesterday_price * 100)
    if percentage >= PRICE_JUMP:
        if difference < 0:
            trend = "🔻"
        stock_info = {
            "stock_news": True,
            "trend": trend,
            "value": round(percentage, 2),
        }


def create_news():
    news_params = {
        "q": QUESTION,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": news_api_key,
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    news_for_sms = []
    for i in range(NUM_ARTICLES):
        message = {
            "title": articles[i]["title"],
            "description": articles[i]["description"]
        }
        news_for_sms.append(message)
    return news_for_sms


def send_sms(information, stock):
    client = Client(account_sid, auth_token)
    for info in information:
        body = (f"📈TSLA: {stock['trend']}{stock['value']}%\n"
                f"Headline: {info['title']}\n"
                f"Brief: {info['description']}")
        message = client.messages \
            .create(
                body=body,
                from_="+13513005694",
                to=phone
            )
        print(message.status)


yesterday = dt.datetime.now().date() - dt.timedelta(days=1)
calculate_stock_price()
if stock_info["stock_news"]:
    news = create_news()
    send_sms(news, stock_info)
