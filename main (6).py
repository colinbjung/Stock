# https://www.tradingview.com/symbols/NASDAQ-TSLA/
# https://www.alphavantage.co/ <--- GET YOUR FREE API KEY TODAY

STOCK_API = "99HGUVV6BNO6X1MO"
# https://newsapi.org/ <---- GET API KEY
NEWS_API = "f793718a97544a3bb348f63cef3b0a8c"
# https://www.twilio.com/ <-- Sign up and start building 
TWIL_SID = "AC1642761657534953e9e1ee3cce685a27"
TWIL_AUTH = "6419c20531edbf2cfadb958bdab706ec"
TWIL_NUM = "8065152243"
VERIFIED_NUMBER = "3343225695"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


import requests

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=99HGUVV6BNO6X1MO'
# r = requests.get(url)
# data = r.json()

# print(data)




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#Get yesterday's closing stock price

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



# #TODO 2. - Get the day before yesterday's closing stock price

# daybeforeyesterday_data = data_list[1]
# daybeforeyesterday_closing_price = daybeforeyesterday_data["4. close"]
# print(daybeforeyesterday_closing_price)


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# diff = abs(float(yesterday_closing_price) - float(daybeforeyesterday_closing_price))
# print(diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# diff_percent = ((diff / float(yesterday_closing_price)) * 100)
# print(diff_percent)

# percentdiff = ((float(daybeforeyesterday_closing_price) / float(yesterday_closing_price)) - 1) * 100
# print(str(percentdiff) + '%')

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# news_params = {
#   "qInTitle": STOCK_NAME,
#   "apikey": NEWS_API
# }
# response = requests.get(NEWS_ENDPOINT, params = news_params)
# data = response.json()['articles']
# news1 = data[0]
# news1title = news1['title']
# news1description = news1['description']
# news2 = data[1]
# news2title = news2['title']
# news2description = news2['description']
# news3 = data[2]
# news3title = news3['title']
# news3description = news3['description']
# print('Title - {}: Description - {}\nTitle - {}: Description - {}\nTitle - {}: Description - {}'.format(news1title, news1description, news2title, news2description, news3title, news3description))

# KEYWORD = input('Search for a company name: ')

# search_params = {
#   "function": "SYMBOL_SEARCH",
#   "keywords": KEYWORD,
#   "apikey": STOCK_API
# }

# response = requests.get(STOCK_ENDPOINT, params = search_params)
# data = response.json()['bestMatches']
# result1 = data[0]
# result1symbol = result1['1. symbol']
# result1name = result1['2. name']
# result2 = data[1]
# result2symbol = result2['1. symbol']
# result2name = result2['2. name']
# print('1. Name - {}: Symbol - {}\n2. Name - {}: Symbol - {}'.format(result1name, result1symbol, result2name, result2symbol))

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
  


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# Prompts the user 
STOCK_NAME = search(input("Type a company name to search for: "))
closingprice(STOCK_NAME)



