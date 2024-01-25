import smtplib
from config import email_ID,email_provider,password
from src.Scraping import Scrape
import time 
buy_price = 60.00      #target price

link = input("Enter the URL of your desired item on amazon : ")
#example URL : https://www.amazon.com/Glorious-Gaming-Mouse-Model-Matte/dp/B08HR9S2B7/ref=sr_1_4?crid=2GLDDOL18GVDY&keywords=glorious%2Bmodel%2Bo&qid=1705853096&sprefix=glorious%2Bmodel%2Bo%2Caps%2C284&sr=8-4&th=1

#create object item
item = Scrape(link=link)

#initializing a while loop
while True:

    if item.price() <= buy_price:       #check for the current price

        message = f"YAyy your {item.title()} is waiting for you in just ${item.price()} "

        with smtplib.SMTP(email_provider, port= 587) as connection:             #setup a connection with the mail server
            connection.starttls()                                       #transfer layer security
            result = connection.login(user= email_ID, password= password)       #login

            connection.sendmail(                                        #send mail
                from_addr= email_ID,
                to_addrs= email_ID,
                message = f"AMAZON PRICE ALERT!! \n {message}"
            )
    
    time.sleep(60)                  #make the loop sleep for 60 seconds after every run

