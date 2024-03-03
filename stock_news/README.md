# Stock News

## Behavior the app
1. Application connects with the alphavantage API (stock endpoint) and check Tesla stock quotes for yesterday price and two days ego price.
2. If the difference between the stock price is greater/less than 1, the application:
   * Connects to newsapi endpoint and search by question *"+Tesla Inc OR +Musk OR +TSLA"* 3 news
   * App are sending 3 SMSs. Each SMS inform about value of trends, headline and short brief news