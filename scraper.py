import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    URL = 'https://www.amazon.in/gp/product/B07VNS5QQN/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1'
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    page = requests.get(URL, headers = headers)
    ## beautifulsoup parses the page and take out different instances out of it
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    title = soup.find(id = "productTitle")
    print(title.get_text().strip())
    price =soup.find(id = "priceblock_ourprice").get_text()
    #print(price.strip())
    ##this price is a string i cant use it for comparison
    converted_price = float(price[3] + price[5:8]) ##convert to float here only
    #print(converted_price)
    if(converted_price < 3900):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    ##smtp takes two arguements, smtp address of the mailing service and
    ##connection number
    server.ehlo()
    ##command sent by email server to receiving email server
    server.starttls()
    server.ehlo()
    server.login('adityarrj@gmail.com' ,'cxmlrsegygkebeit')
    ## now we make the contents of the mail
    subject = 'hey the price fell down'
    body = 'check the amazon link here - https://www.amazon.in/gp/product/B07VNS5QQN/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "adityarrj@gmail.com",
        "itiheena2714@gmail.com",
        msg
    )
    print('Hey email has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)