from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class Fnac(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.fnac.es/SearchResult/ResultList.aspx?SCat=0%211&Search="
		self.separator="+"
		self.query=query

	def get_url(self):
		query=self.query.replace(" ",self.separator)
		return self.head+query

	def get_price(self):
		url=self.get_url()
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			first_price=soup.find_all("a", {"class": "userPrice"})[0].text
			first_url=soup.find_all("a", {"class": "userPrice"})[0].attrs["href"]
			first_name=soup.find_all("a",{"class":"js-minifa-title"})[0].text
			return (first_price,first_url,first_name)
		except:
			return ("No se ha podido conseguir el precio",url,query)