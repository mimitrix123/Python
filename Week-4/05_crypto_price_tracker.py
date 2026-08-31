"""Week 4 Practice 5: Live Cryptocurrency Price Tracker."""

import requests


def get_price(coin="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url, timeout=10)
    data = response.json()
    if coin in data:
        print(f"{coin.title()} Price: {data[coin][currency]} {currency.upper()}")
    else:
        print("Unable to fetch price.")


if __name__ == "__main__":
    get_price(input("Enter coin name (bitcoin, ethereum, dogecoin): ").lower())
