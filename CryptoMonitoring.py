import requests
from datetime import datetime

# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR

URL = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"


def get_price(coin, currency):
    try:
        respone = requests.get(URL.format(coin, currency)).json()
        return respone
    except:
        return False


Input1 = input("Select coin (BTC,ETH,LTC,XRP): ")
Input2 = input("Select currency (USD,JPY,EUR): ")

while True:
    date = datetime.now()
    date = date.strftime("%d/%B/%Y %H:%M:%S")
    current_price = get_price(Input1, Input2)
    if current_price:
        print(date, current_price[Input2])
