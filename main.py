import requests
from bs4 import BeautifulSoup 
import smtplib

my_email = ""
password= ""


URL="https://www.amazon.com/Logitech-Master-Advanced-Wireless-Mouse/dp/B07XC2FWD1"
LANGUAGE= "en-US,en;q=0.9,ro;q=0.8"
AGENT= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
DESIRED_PRICE= 100

response= requests.get(URL, headers= {'Accept-Language' : LANGUAGE,
            'User-Agent': AGENT})
soup= BeautifulSoup(response.text,"html.parser")
price= float(soup.find(name="span",class_="a-offscreen").getText().replace('$',""))
print(price)

if price<= DESIRED_PRICE:
    message= f"Your product is under your desired price{DESIRED_PRICE} ! GO GET IT! {URL}"
    with  smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)

            connection.sendmail(
                from_addr =  my_email,
                to_addrs= "",
                msg= f"Subject:Cheap Product\n\n {message}")

