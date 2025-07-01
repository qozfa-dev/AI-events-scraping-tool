import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


url = 'https://react-amazon-bestsellers-books-dy.netlify.app/'

session = HTMLSession()
response = session.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.find_all('article', class_='book'))
