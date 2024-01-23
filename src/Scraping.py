from bs4 import BeautifulSoup
import requests
import lxml 

#initialize a class 
class Scrape:

    headers = {
    "User-Agent" : "YOUR User-Agent",
    "Accept-Language" : "en-US,en;q=0.9"
    }                               #class attribute


    def __init__(self,link):            #define object initializer with 
        self.link = link
        
    #instance menthods
    def content(self):
        '''
            Returns the html of the web page
        '''
        response = requests.get(self.link)
        return response.text
    
    def price(self,content):

        '''
            Returns the price of the 
            Argument : content
        '''

        self.soup = BeautifulSoup(content,"lxml")
        price = self.soup.select_one(".a-price.a-text-price.a-size-medium.apexPriceToPay .a-offscreen")
        return float(price.getText()[1:])
    
    def title(self, content):
        '''
            Returns the name of the item
            Argument : content
        '''
        self.soup = BeautifulSoup(content,"lxml")
        title = self.soup.select_one("#titleSection")
        real_title = title.getText().strip()
        return real_title




