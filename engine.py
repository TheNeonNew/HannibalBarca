# engine for game logic
import HB_classLib as cllib


class Engine:
    """Engine which will calculate gameClasses's interactions"""
    def __init__(self):
        self.pl = cllib.Player()
        self.map = cllib.Map()
        self.lvls = [cllib.ButtonTutorial, cllib.ButtonLvl1,
                     cllib.ButtonLvl2, cllib.ButtonLvl3]
        self.start_cards = [cllib.MeleeCard("HB_army", health=5,attack=3),
                            cllib.CavalryCard("horse", health=3, attack=3),
                            cllib.CavalryCard("elephant", health=5, attack=4)]
    def start(self):
        self.pl.hand.fill(self.start_cards)
        self.map.fill_with(self.lvls)
        
    
