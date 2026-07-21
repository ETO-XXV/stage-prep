import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://quotes.toscrape.com/"

response = requests.get(url)

# pprint(response.text) 


soup = BeautifulSoup(response.text, "html.parser")
first_quote_tag = soup.find("span" , class_="text")

print(first_quote_tag.text)

