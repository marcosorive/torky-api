from amazon.api import AmazonAPI
import bottlenose.api
from GamePriceScrapper import GamePriceScrapper


class Amazon(GamePriceScrapper):

	def __init__(self,query):
		super().__init__()
		self.head="https://www.amazon.es/s/ref=nb_sb_noss?field-keywords="
		self.separator="+"
		self.query=query
	
	def get_url(self):
		query=self.query.replace(" ",self.separator)
		return self.head+query
	
	def get_price(self):
		url=self.get_url()
		try:	
			amazon = AmazonAPI("", "", "", region="")
			region_options = bottlenose.api.SERVICE_DOMAINS.keys()
			products = amazon.search_n(1,Keywords=self.query, SearchIndex='VideoGames')
			price=products[0].price_and_currency
			if price[0]==None:
				return ("No se ha podido conseguir el precio",url,self.query)
			else:
				price=str(price[0]).replace(".",",") + "€"

			return (price,products[0].offer_url,products[0].title)
		except Exception as e:
			return ("No se ha podido conseguir el precio",url,self.query)