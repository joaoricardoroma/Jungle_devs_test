from __future__ import absolute_import, unicode_literals
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models import Author, Article
from django.core.management.base import BaseCommand
from selenium.webdriver.chrome.options import Options
from app.tasks import bsoup


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bsoup.delay()

