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
print('test before the loop / page 1')

for i in items:
    name=i.find('h4',class_='').text
    print(name)
    price=i.find('h5',class_='').text
    print(price)

print('test after the loop')

#Getting the other pages:
#The url for all pages is set as a string
baseURL="https://scrapingclub.com"
#The endpoints for each url are found from the pages section using the tag <a>
pages=sourceCode.find('nav',class_='pagination')
endpoints=pages.find_all('a')
for tag in  endpoints[:-1]:
    #Here the part saved in the href is extracted
    href = tag.get("href")
    #Here the links for each page is created using the base url & endpoint
    link=baseURL+href
    # here a request with the new link is made
    newResponse = requests.get(link)
    #Here the response is parsed using lxml
    newSourceCode = BeautifulSoup(newResponse.text,'lxml')
    #Items are found, here we get both the name and price of te items
    newItems = newSourceCode.find_all('div',class_='w-full rounded border')
    #Now we iterate through the items to individually get the name and price
    print('\nHere page #' + str(tag.text) + ' is shown\n')
    for i in newItems:
        name2=i.find('h4',class_='').text
        print(name2)
        price2=i.find('h5',class_='').text
        print(price2)   