import csv
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

url = 'https://www.flipkart.com/realme-6-comet-blue-128-gb/p/itm50e6d62dcf5ee?pid=MOBFPCX72FYWY7NF&lid=LSTMOBFPCX72FYWY7NFADYHCJ&marketplace=FLIPKART&srno=b_1_1&otracker=hp_banner_1_7.bannerX3.BANNER_LRTM1LIBOB16&fm=neo%2Fmerchandising&iid=cfad56f3-2c71-49d6-85cf-4d33893c1d56.MOBFPCX72FYWY7NF.SEARCH&ppt=browse&ppn=browse&ssid=xyfmf6v2v40000001603175905248'

while True:
    uClient = urlopen(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, 'html.parser')

    if page_soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text.split("₹")[1]:
        price = page_soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text.split("₹")[1]
        print(price)
        localtime = time.localtime()
        currtime = time.strftime("%I:%M:%S %p", localtime)
        tup = (price, currtime)
        f = open('prices.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(tup)
        f.close()
        time.sleep(1)