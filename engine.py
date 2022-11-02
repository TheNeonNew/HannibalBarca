# engine for game logic
import HB_classLib as cllib
from pygame import Color


class Engine:
    """Engine which will calculate gameClasses's interactions"""
    def __init__(self, screen, mode=1):

        self.screen = screen
        
        self.pl = cllib.Player()
        self.map = cllib.Map()
        self.currlvlmap = cllib.LvlMap()
        #TODO: replace cllib.ButtonTutorial with cllib.Button(...)
        self.mod_buttons = [cllib.Button((300, 340), (100, 60), Color("gold"), "Divided field", None, 18),
                            cllib.Button((300, 420), (100, 60), Color("gold"), "No man's land", None, 18)]
##        self.start_cards = [cllib.MeleeCard("king", 5,3),
##                            cllib.CavalryCard("horse", 3, 3),
##                            cllib.CavalryCard("elephant", 5, 4)]
        self.start_cards = None
        self.borderline = cllib.Line(self.screen, [400, 0, 400, 480], "red", 3)
        self.blno_mans_land = [cllib.Line(self.screen, [240, 0, 240, 480], "blue", 3), cllib.Line(self.screen, [620, 0, 620, 480], "red", 3)]
        self.mode = mode
    def start(self):
        self.pl.hand.append(self.start_cards)
        self.map.fill_with(self.mod_buttons)
        self.map.draw(self.screen)

    def turn_level(self):
        self.map.should_draw = False
        self.currlvlmap.gen(self.pl)
        self.currlvlmap.draw(self.screen)

    def update_map(self):
        self.map.draw(self.screen)

    def update_level(self):
        self.currlvlmap.draw(self.screen)
        match self.mode:
            case 1:
                self.borderline.draw()
            case 2:
                for el in self.blno_mans_land:
                    el.draw()
        
        
        
    
