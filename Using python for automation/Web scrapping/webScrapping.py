import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
#A get request is sent and saved
response = requests.get(url)
#Beautiful soup and lxml are used to parse the answer
sourceCode = BeautifulSoup(response.text,'lxml')
#The source code is filtered by usin the find all function
quotes = sourceCode.find_all('span', class_='text')
#The authors are retrieved too
authors=sourceCode.find_all('small', class_='author')
#Tags are also found, here we get the whole set of tags 
tags = sourceCode.find_all('div',class_='tags')

#The 'text' property of each quote and author is printed looping through their respective lists
for index in range(0,len(authors)):
    print(quotes[index].text)
    print(authors[index].text)
    #Here we filter the tags for each quote
    tagsByQuote=tags[index].find_all('a',class_='tag')
    for i in range(0,len(tagsByQuote)):
        print(tagsByQuote[i].text)



