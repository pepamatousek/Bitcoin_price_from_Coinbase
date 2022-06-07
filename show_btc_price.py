import requests
import time


url = "https://api.coinbase.com/v2/prices/BTC-EUR/buy"
sec = 7

def main(url, sec):
    while True:
        coinbase = requests.get(url)
        to_json = coinbase.json()
        price = to_json["data"]["amount"]
        currency = to_json["data"]["currency"]
        print(f"Current bitcoin buy price from Coinbase is {price} {currency}")
        time.sleep(sec)


if __name__ == "__main__":
    main(url, sec)

