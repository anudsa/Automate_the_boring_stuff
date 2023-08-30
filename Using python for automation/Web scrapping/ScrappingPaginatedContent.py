#Scrapping paginated content
import requests
from bs4 import BeautifulSoup
url='https://scrapingclub.com/exercise/list_basic/?page=1'
#A get request is sent and saved
response = requests.get(url)
#Beautiful soup and lxml are used to parse the answer
sourceCode = BeautifulSoup(response.text,'lxml')
#Items are found, here we get both the name and price of te items
items = sourceCode.find_all('div',class_='w-full rounded border')
#Now we iterate through the items to individually get the name and price
for i in items:
    name=i.find('h4',class_='').text
    print(name)
    price=i.find('h5',class_='').text
    print(price)

#Getting the other pages:
baseURL="https://scrapingclub.com"
pages=sourceCode.find('nav',class_='pagination')
print("\n")
endpoints=pages.find_all('a')
for tag in  endpoints[:-1]:
    href = tag.get("href")
    print(href)
    link=[baseURL+href]
    print(link)

"""
    #a request is made for each page link and
    response = requests.get(link)
    #Beautiful soup and lxml are used to parse the answer
    sourceCode = BeautifulSoup(response.text,'lxml')
    #Items are found, here we get both the name and price of te items
    items = sourceCode.find_all('div',class_='w-full rounded border')
    #Now we iterate through the items to individually get the name and price
    for i in items:
        name=i.find('h4',class_='').text
        print(name)
        price=i.find('h5',class_='').text
        print(price)
"""