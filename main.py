import requests
from bs4 import BeautifulSoup
import selenium
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')

articles = soup.find_all('tm-articles-list__item')
for article in articles:
    article_name = article.find(
        class_="tm-article-snippet__title tm-article-snippet__title_h2")
    article_time = article.find(class_="tm-article-snippet__datetime-published")
    article_name = article_name.text
    href = article_name.find(class_="tm-article-snippet__title-link")
    url = 'https://habr.com/ru/post/' + href.attrs['href'].split('/')[-2] + '/'
    article_time = article_time.next.attrs['title']
    for word in KEYWORDS:
        if word in article_name:
            print(f'<{article_time}> - <{article_name}> - <{url}>')
            break
