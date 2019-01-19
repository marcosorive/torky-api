from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class InstantGaming(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.instant-gaming.com/es/busquedas/?q="
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
			first_price=soup.find_all("div",{"class":"item mainshadow"})[0].attrs["data-price"]
			first_price=first_price.replace(".",",")+"€"
			first_url=soup.find_all("a",{"class":"cover"})[0].attrs["href"]
			first_name=soup.find_all("div",{"class":"name"})[0].text
			return (first_price,first_url+"?igr=morive02-21",first_name)
		except:
			return ("No se ha podido conseguir el precio",url,self.query)