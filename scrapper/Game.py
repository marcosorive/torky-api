from bs4 import BeautifulSoup
from selenium import webdriver
from lxml.html import fromstring
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from GamePriceScrapper import GamePriceScrapper

class Game(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.game.es/buscar/"
		self.separator="-"
		self.query=query

	def get_url(self):
		search=self.query.replace(" ",self.separator)
		return self.head+search

	def get_price(self):
		#export PATH=$PATH:/home/marcos/geckodriver/geckodriver
		#Put geckodriver in usr/local/bin
		search_url=self.get_url()
		fails=0
		while True:
			try:	
				ua=UserAgent()
				options=Options()
				options.add_argument("--headless")
				driver = webdriver.Chrome(chrome_options=options)
				driver.implicitly_wait(10)
				driver.get(search_url)
				body=driver.find_element_by_tag_name("body")
				soup=BeautifulSoup(body.get_attribute('innerHTML'),'html.parser')
				game_page=soup.find_all("a",{"class":"a cm-txt"})[0].attrs["href"]
				game_name=soup.find_all("a",{"class":"a cm-txt"})[0].text
				break
			except Exception as e:
				print(e)
				fails=fails+1
				if(fails>10):
					return ("No se ha podido conseguir el precio",search_url,self.query)
		product_url=""
		while True:
			try:
				product_url="https://game.es"+game_page
				fails=0
				ua=UserAgent()
				options=Options()
				options.add_argument("--headless")
				driver = webdriver.Chrome(chrome_options=options)
				driver.implicitly_wait(10)
				driver.get(product_url)
				body=driver.find_element_by_tag_name("body")
				soup=BeautifulSoup(body.get_attribute('innerHTML'),'html.parser')
				price=soup.find_all("span",{"class":"buy--info"})[0].text
				break
			except Exception as e:
				print(e)
				fails=fails+1
				if(fails>10):
					return ("No se ha podido conseguir el precio",product_url,self.query)
		return (price[25:33],product_url,game_name)