import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())

res = soup.title

print (soup.get_text())