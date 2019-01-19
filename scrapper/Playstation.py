from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class Playstation(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://store.playstation.com/es-es/search/"
		self.separator="%20"
		self.query=query

	def get_url(self):
		query=self.query.replace(" ",self.separator)
		return self.head+query

	def get_price(self):
		url=self.get_url()
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			first_price=soup.find_all("h3", {"class": "price-display__price"})[0].text.split("\xa0")[0]+"€"
			first_url=soup.find_all("a", {"class": "internal-app-link ember-view"})[1].attrs["href"]
			first_url="https://store.playstation.com"+first_url
			first_name=soup.find_all("div", {"class": "grid-cell__title"})[0].findChildren()[0].text
			return (first_price,first_url,first_name)
		except Exception as e:
			print(e)
			return ("No se ha podido conseguir el precio",url,self.query)