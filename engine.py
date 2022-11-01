# engine for game logic
import HB_classLib as cllib


class Engine:
    """Engine which will calculate gameClasses's interactions"""
    def __init__(self, screen):

        self.screen = screen
        
        self.pl = cllib.Player()
        self.map = cllib.Map()
        self.currlvlmap = cllib.LvlMap()
        #TODO: replace cllib.ButtonTutorial with cllib.Button(...)
##        self.lvls = [cllib.ButtonTutorial, cllib.ButtonLvl1,
##                     cllib.ButtonLvl2, cllib.ButtonLvl3]
##        self.start_cards = [cllib.MeleeCard("king", 5,3),
##                            cllib.CavalryCard("horse", 3, 3),
##                            cllib.CavalryCard("elephant", 5, 4)]
        self.start_cards = None
        self.borderline = cllib.Line(self.screen, [400, 0, 400, 480], "red", 3)
    def start(self):
        self.pl.hand.append(self.start_cards)
##        self.map.fill_with(self.lvls)
##        self.map.draw(self.screen)

    def turn_level(self):
        self.map.should_draw = False
        self.currlvlmap.gen(self.pl)
        self.currlvlmap.draw(self.screen)

    def update_level(self):
        self.currlvlmap.draw(self.screen)
        self.borderline.draw()
        
        
        
    
