from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models import Author, Article
from django.core.management.base import BaseCommand
from selenium.webdriver.chrome.options import Options


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        page = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
        links = self.get_links(page)
        driver = webdriver.Chrome(options=self.set_chrome_options())
        self.web_scrap(links)

    def set_chrome_options(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options

    def get_links(self, page):
        url = requests.get(page).text
        soup = BeautifulSoup(url, 'lxml')
        movies = soup.find_all('td', class_='titleColumn')
        links = []
        for movie in movies:
            link = 'https://www.imdb.com' + movie.a['href']
            link_list = {'link': link, }
            links.append(link_list)
        return links

    def web_scrap(self, links):
        articles = []
        for web in links[:10]:
            driver = webdriver.Chrome(options=self.set_chrome_options())
            page = web['link']
            url = requests.get(page).text
            soup = BeautifulSoup(url, 'lxml')
            sleep(3)
            author_name = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
            category = soup.find('a', class_="sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt").text
            title = soup.find('h1').text
            summary = soup.find('span', class_="sc-16ede01-2 gXUyNh").text
            driver.get(page)
            section = driver.find_element(By.CSS_SELECTOR, 'section[data-testid="Storyline"]')
            body = section.find_element(By.CLASS_NAME, 'ipc-html-content-inner-div').text
            # body = soup.find('div', class_='ipc-html-content-inner-div').text
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
                Article.objects.create(author_id=author_id, category=category, title=title, summary=summary, first_paragraph=firstParagraph, body=body)