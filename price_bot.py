import requests
import time
import datetime

from bs4 import BeautifulSoup


dt_India = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')


URL="http://rubberboard.org.in/public"

headers={
  "User-Agent": 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
} 


def checkprice():

    page=requests.get(URL, headers=headers) 

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="loc1").get_text().strip()

    price1=int(float(price[24:31]))/100
    price2=int(float(price[46:54]))/100


    converted_price1="FIRST_QUALITY == "+str(price1)


    converted_price2="SECOND_QUALITY == "+str(price2)

    

    print(converted_price1)
    print(converted_price2)

    requests.post("https://api.telegram.org/Your-bot-id:API-TOKEN/sendMessage?chat_id=YOUR-CHAT-ID&text={}%0d%0a%0d%0a{}%0d%0a%0d%0a{}".format(Indian_time,converted_price1,converted_price2))

while True:
    checkprice()
    time.sleep(28800)