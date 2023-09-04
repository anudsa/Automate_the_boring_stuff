import requests
requestURL='https://api.upcitemdb.com/prod/trial/lookup'
upcInfo = {'upc': '194253416982'}
#get query is made, the dictionary info is sent as parameters
query = requests.get(requestURL,params=upcInfo)
print(query.url)
#data is parsed as json
content=query.json()
#the info is stored in a dictionary inside another dictionary
items=content['items']
#accesing second dictionary info
itemsData=items[0]
#saving the title and prics
itemTitle=itemsData['title']
itemPrice=itemsData['offers'][1]['price']
print('The item is: \n'+itemTitle)
print('The price is: \n$'+str(itemPrice))