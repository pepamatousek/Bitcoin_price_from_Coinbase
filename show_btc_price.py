import requests


from os import system
from bs4 import BeautifulSoup
from datetime import datetime


url = "https://www.tradingview.com/chart/?symbol=BITSTAMP%3ABTCEUR"


def main():
    print(timer())


def timer(): 
    while True:
        sec = int(datetime.now().strftime("%S"))
        sec_5 = sec % 5
        if sec_5 == 0:
            return True


# if timer() == True:
#     print("5s")

if __name__ == "__main__":
    main()

