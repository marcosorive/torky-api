from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
import requests
from amazon.api import AmazonAPI
import bottlenose.api
from selenium import webdriver
from lxml.html import fromstring
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class GamePriceScrapper:

	def get_response(self,url):
		ua=UserAgent()
		header={'User-Agent':ua.random}
		r = requests.get(url,headers=header)
		return r

	def get_url(self):
		query=self.query.replace(" ",self.separator)
		return self.head+query

	

