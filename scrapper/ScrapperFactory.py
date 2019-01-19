from Fnac import Fnac
from Amazon import Amazon
from Game import Game
from InstantGaming import InstantGaming
from CorteIngles import CorteIngles
from Steam import Steam
from Nintendo import Nintendo
from Playstation import Playstation
from Xbox import Xbox


class ScrapperFactory:

    def __init__(self):
        pass
        
    def buildScrapper(self,query,store):
        if store=="fnac":
            return Fnac(query)
        elif store=="amazon":
            return Amazon(query)
        elif store=="game":
            return Game(query)
        elif store=="instant_gaming":
            return InstantGaming(query)
        elif store=="corte_ingles":
            return CorteIngles(query)
        elif store=="steam":
            return Steam(query)
        elif store=="nintendo":
            return Nintendo(query)
        elif store=="playstation":
            return Playstation(query)
        elif store=="xbox":
            return Xbox(query)
        else:
            raise NameError("Store not defined")