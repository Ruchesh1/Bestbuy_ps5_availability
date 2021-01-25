import requests
from bs4 import BeautifulSoup
from threading import Timer
import winsound

item_status = ' '
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def item_search(url): 
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='root')
    product_elems = results.find('span', class_='availabilityMessage_ig-s5 container_3LC03')
    availability = product_elems.text.strip()
    return availability

def item_availability():
    link = 'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185'
    item_avail = item_search(link)
    if item_avail == "Coming soon":
        print("Out Of Stock")
    elif item_availability == "Available to ship":
        print("In Stock!!!")
        winsound.PlaySound("*", winsound.SND_ALIAS)
    else:
         print("Error!")
    Timer(5, item_availability()).start()


print(item_availability())
