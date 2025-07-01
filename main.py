import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


url = 'https://react-amazon-bestsellers-books-dy.netlify.app/'

session = HTMLSession()
response = session.get(url)
response.html.render()

print(response.html)
print(response.html.html)

# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.find_all('article', class_='book'))

# 8.30
