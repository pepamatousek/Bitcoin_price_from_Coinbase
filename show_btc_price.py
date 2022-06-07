import requests
import time


url = "https://api.coinbase.com/v2/prices/spot?currency=EUR"
sec = 7

def main(url, sec):
    while True:
        coinbase = requests.get(url)
        to_json = coinbase.json()
        price = to_json["data"]["amount"]
        currency = to_json["data"]["currency"]
        print(f"Current bitcoin price from Coinbase is {float(price):.2f} {currency}")
        time.sleep(sec)


if __name__ == "__main__":
    main(url, sec)

