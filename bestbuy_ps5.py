import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
url = 'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185'
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='root')
product_elems = results.find('span', class_='availabilityMessage_ig-s5 container_3LC03')
availability = product_elems.text.strip()

if availability == "Coming soon":
    print("Out Of Stock")
elif availability == "Available to ship":
    print("In Stock!!!")  
else:
    print("Error!")
