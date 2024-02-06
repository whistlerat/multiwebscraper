import requests
from bs4 import BeautifulSoup
import pandas as pd

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

box = soup.find('article',{'class':'main-article'})
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script')
transcript = transcript.get_text(strip=True, separator=" ")



df = pd.DataFrame({'Title':title, 'Transcript':transcript}, index=[0])
df.to_csv('transcript.csv', index=False, encoding='utf-8')
