import requests
from bs4 import BeautifulSoup
import pandas as pd

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')

link = box.find_all('a', href=True)
lists = []
for link in box.find_all('a', href=True):
    lists.append(link['href'])

all_movies = []
for link in lists:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article',{"class":"main-article"})

    title = box.find('h1').get_text()
    transcript = box.find('div', {"class":"full-script"})
    transcript = transcript.get_text(strip=True, separator=' ')
    list_append = [title, transcript]
    all_movies.append(list_append)

titles_only = [item[0] for item in all_movies]
# print(titles_only)
print(len(titles_only))
# print(all_movies)