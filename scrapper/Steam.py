from bs4 import BeautifulSoup
from GamePriceScrapper import GamePriceScrapper

class Steam(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://store.steampowered.com/search/?term="
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
			first_game=soup.find_all("a",{"class":"search_result_row ds_collapse_flag "})[0]
			if(len(first_game)>0):
				link=first_game.attrs["href"]
				name=first_game.findChildren("span",{"class":"title"})[0].text
				discounted=first_game.find_all("div",{"class":"col search_price discounted responsive_secondrow"})
				if(discounted):
					discounted=discounted[0]
					price=str(discounted.text).split("€")[1] + "€"
					return(price,link,name)
				else:
					price=first_game.findChildren("div",{"class":"col search_price responsive_secondrow"})[0]
					return(str(price.text).strip("\r").strip("\n").strip("\t"),link,name)
			else:
				return ("No se ha podido conseguir el precio",url,self.query,"No juegos")
		except Exception as e:
			print(e)
			return ("No se ha podido conseguir el precio",url,self.query)
		return ("No se ha podido conseguir el precio",url,self.query,"Final")