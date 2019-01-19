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

class Nintendo(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.nintendo.es/Buscar/Buscar-299117.html?q="
		self.separator="%20"
		self.query=query

	def get_url(self):
		query=self.query.replace(" ",self.separator)
		return self.head+query

	def get_price(self):
		url=self.get_url()
		fails=0
		while True:
			try:	
				options=Options()
				options.add_argument("--headless")
				driver = webdriver.Chrome(chrome_options=options)
				driver.implicitly_wait(5)
				driver.get(url)
				body=driver.find_element_by_tag_name("body")
				soup=BeautifulSoup(body.get_attribute('innerHTML'),'html.parser')
				file=open("nintendo.hml","w")
				file.write(str(soup))
				file.close()
				price=soup.find_all("ul",{"class":"results"})[1]
				price=price.findChildren("div",{"class":"col-xs-12 col-sm-10 col-sm-offset-1 col-lg-8 col-lg-offset-2"})[0]
				print(price)
				price=price.findChildren("p",{"class":"page-data-purchase"})
				if(price):
					print(price)
					break
				fails=fails+1
				if(fails>10):
					return ("No se ha podido conseguir el precio",url,self.query)
			except Exception as e:
				print(e)
				fails=fails+1
				if(fails>15):
					return ("No se ha podido conseguir el precio",url,self.query)