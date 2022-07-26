#APIs and websites to be implemented when using get requests
STOCK_API = "99HGUVV6BNO6X1MO"
NEWS_API = "f793718a97544a3bb348f63cef3b0a8c"
TWIL_SID = "AC1642761657534953e9e1ee3cce685a27"
TWIL_AUTH = "6419c20531edbf2cfadb958bdab706ec"
TWIL_NUM = "8065152243"
VERIFIED_NUMBER = "3343225695"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


import requests

# finds the closing price of a specific stock name
def closingprice(STOCK_NAME):
  stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
  }
  response = requests.get(STOCK_ENDPOINT, params=stock_params)
  data = response.json()["Time Series (Daily)"]
  data_list = [value for (key, value) in data.items()]
  yesterday_data = data_list[0]
  yesterday_closing_price = yesterday_data["4. close"]
  print("Yesterday's closing price for {} was {}".format(STOCK_NAME, yesterday_closing_price))

# based on user input of a company name, finds the top results ( up to 10 ) 
def search(compName):
  search_params = {
  "function": "SYMBOL_SEARCH",
  "keywords": compName,
  "apikey": STOCK_API
}
  response = requests.get(STOCK_ENDPOINT, params = search_params)
  data = response.json()['bestMatches']
  names = []
  symbols = []
  for x in range(len(data)):
    result = data[x]
    resultsymbol = result['1. symbol']
    symbols.append(resultsymbol)
    resultname = result['2. name']
    names.append(resultname)
  if len(symbols) < 10:
    # prompts user on which result matches their desired outcome
    for x in range(len(symbols)):
      print('{}. NAME - {}\n   SYMBOL - {}\n'.format(x + 1, names[x], symbols[x]))
    userNum = int(input("Enter the number that corresponds to your desired company: "))
    userSym = symbols[userNum - 1]
    return userSym
  elif len(symbols) >= 10:
    for x in range(10):
      print('{}. NAME - {}\n   SYMBOL - {}\n'.format(x + 1, names[x], symbols[x]))
    userNum = int(input("Enter the number that corresponds to your desired company: "))
    userSym = symbols[userNum - 1]
    return userSym
   
# Prompts the user to search for a company and returns their closing price
STOCK_NAME = search(input("Type a company name to search for: "))
closingprice(STOCK_NAME)




