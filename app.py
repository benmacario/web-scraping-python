import requests
from bs4 import BeautifulSoup

response = requests.get('https://animesonline.cc/animes-mais-vistos/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

post = site.find('div', attrs={'class': 'wp-content'})

data_title = post.find('div', attrs={'class': 'data'})

title = data_title.find('a')

print('Titulo do anime: ', title.text)
