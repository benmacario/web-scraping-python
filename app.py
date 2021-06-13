import requests
from bs4 import BeautifulSoup

response = requests.get('https://animesonline.cc/animes-mais-vistos/')

data = []

content = response.content

site = BeautifulSoup(content, 'html.parser')

wp_content = site.find('div', attrs={'class': 'wp-content'})

archive_contents = wp_content.findAll('div', attrs={'id': 'archive-content'})

for archive_content in archive_contents:
    data_anime = archive_content.find('div', attrs={'class': 'poster'})

    info_anime = data_anime.find('img')

    data.append({
        'titulo': info_anime['alt'],
        'image_capa': info_anime['src'],
    })

print(data)
