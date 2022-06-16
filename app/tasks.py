from __future__ import absolute_import, unicode_literals
from project.celery import app
import requests
from django.core.management.base import BaseCommand
from app.models import Author, Article
from project.celery import app
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models import Author, Article
from django.core.management.base import BaseCommand
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@app.task(name='web_scraping_json')
def json():
    page = 1
    headers = {'User-Agent': 'robo_maldito'}
    response = requests.get(f'https://imasters.com.br/api/articles/?category=back-end&page={page}&per_page=10',
                            headers=headers)
    if response.status_code != 200:
        raise Exception('error ao carregar o site')
    content = response.json()
    max_pages = content['maxPages']

    for page in range(page, 311):
        response = requests.get(f'https://imasters.com.br/api/articles/?category=back-end&page={page}&per_page=10',
                                headers=headers)
        if response.status_code != 200:
            raise Exception('error ao carregar o site')
        content = response.json()
        for article in content['data']:
            author_name = article['author']['name']
            category = article['categories'][0]['title']
            title = article['title']
            body = article['content']
            summary = body[:50]
            firstParagraph = body[:200]
            try:
                author = Author.objects.get(name=author_name)
                author_id = author.id
            except:
                author = Author.objects.create(name=author_name)
                author_id = author.id
            try:
                Article.objects.get(title=title)
                pass
            except:
                Article.objects.create(author_id=author_id, category=category, title=title, summary=summary,
                                       first_paragraph=firstParagraph, body=body)


@app.task(name='web_scraping_bsoup')
def bsoup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    page = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    driver = webdriver.Chrome(options=chrome_options)
    url = requests.get(page).text
    soup = BeautifulSoup(url, 'lxml')
    movies = soup.find_all('td', class_='titleColumn')
    links = []
    for movie in movies:
        link = 'https://www.imdb.com' + movie.a['href']
        link_list = {'link': link, }
        links.append(link_list)
    for web in links:
        page = web['link']
        url = requests.get(page).text
        soup = BeautifulSoup(url, 'lxml')
        author_name = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
        category = soup.find('a', class_="sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt").text
        title = soup.find('h1').text
        summary = soup.find('span', class_="sc-16ede01-2 gXUyNh").text
        driver.get(page)
        section = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section[data-testid="Storyline"]')))
        body = section.find_element(By.CLASS_NAME, 'ipc-html-content-inner-div').text
        firstParagraph = body[:50]
        try:
            author = Author.objects.get(name=author_name)
            author_id = author.id
        except:
            author = Author.objects.create(name=author_name)
            author_id = author.id
        try:
            Article.objects.get(title=title)
            pass
        except:
            Article.objects.create(author_id=author_id, category=category, title=title, summary=summary,
                                   first_paragraph=firstParagraph, body=body)
