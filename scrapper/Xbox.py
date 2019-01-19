from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class Xbox(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.microsoft.com/es-es/search?q="
		self.separator="+"
		self.query=query

	def get_price(self):
		url=self.get_url()
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			section=soup.find_all("section", {"class": "m-product-placement-item f-size-medium context-app"})[0]
			first_url="https:"+section.findChildren("a")[0].attrs["href"]
			first_name=section.findChildren("span",{"class":"c-subheading-6"})[0].text
			first_price=section.findChildren("div",{"class":"c-price"})[0].findChildren("span")[0].text
			return (first_price,first_url,first_name)
		except Exception as e:
			print(e)
			return ("No se ha podido conseguir el precio",url,self.query)