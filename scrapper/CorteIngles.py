from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class CorteIngles(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.elcorteingles.es/videojuegos/search/?s="
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
			first_price=soup.find_all("div",{"class":"product-price"})[0].text
			first_url=soup.find_all("a",{"class":"js-product-click event"})[0].attrs["href"]
			first_name=soup.find_all("a",{"class":"js-product-click event"})[0].text
			return (first_price,"https://www.elcorteingles.es"+first_url,first_name)
		except Exception as e:
			print("Corte ingles:",e)
			return ("No se ha podido conseguir el precio",url,self.query)