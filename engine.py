# engine for game logic
import HB_classLib as cllib
from pygame import Color
from pygame import display


class Engine:
    """Engine which will calculate gameClasses's interactions"""

    def __init__(self, screen, usnames, mode=1):

        self.names_frame = (cllib.Text(usnames[0].get_value(), 36, Color("white")),
                            cllib.Text(usnames[1].get_value(), 36, Color("white")))
        self.screen = screen
        self.pl = cllib.Player()
        self.map = cllib.Map()
        self.currlvlmap = cllib.LvlMap()
        self.mod_buttons = [cllib.Button((260, 340), (300, 90), Color("gold"),
                                         "Divided field", None, 54, xIndF=40, yIndF=30),
                            cllib.Button((260, 450), (300, 90), Color("yellow"),
                                         "No man's land", None, 54, xIndF=20, yIndF=30)]
        self.start_cards = [cllib.MeleeCard(Image_fn="images/card1.jpg", pos=(100, 550), health=5,attack=3),
                            cllib.CavalryCard(Image_fn="images/card2.jpg", pos=(250, 550), health=3, attack=3),
                            cllib.CavalryCard(Image_fn="images/card3.png", pos=(500, 550), health=5, attack=4)]
        self.borderline = cllib.Line(self.screen, [400, 0, 400, 480], "black", 3)
        self.blno_mans_land = [cllib.Line(self.screen, [240, 0, 240, 480], "blue", 3),
                               cllib.Line(self.screen, [560, 0, 560, 480], "red", 3)]
        self.mode = mode
        self.turnButton = cllib.Button((360, 500), (80, 80), Color("#E0FFFF"),
                                       "End Turn", None, 24,
                                       xIndF=5, yIndF=35, shape='round', fontColor="#800000")
        self.turnArrow = cllib.Image("images/turn_arrow.jpg", (360, 580), imSize=(90, 120))
        self.details = self.currlvlmap, self.turnButton, self.turnArrow, self.start_cards

    def start(self):
        self.pl.hand.append(self.start_cards)
        self.map.fill_with(self.mod_buttons)
        self.map.draw(self.screen)

    def turn_level(self):
        self.map.should_draw = False
        for btn in self.mod_buttons:
            btn.keepOn = False
        self.currlvlmap.gen(self.pl)
        self.currlvlmap.draw(self.screen)

    def update_map(self):
        self.map.draw(self.screen)

    def update_level(self):
        for det in self.details:
            if det is self.start_cards or isinstance(det, list | tuple):
                for atom in det:
                    atom.draw(self.screen)
                
            else:
                det.draw(self.screen)
            
        match self.mode:
            case 1:
                self.borderline.draw()
                for i, name in enumerate(self.names_frame):
                    self.screen.blit(name.image, (200 + i * 400 - len(str(name.text)) * 6, 500))
            case 2:
                for el in self.blno_mans_land:
                    el.draw()
                for j, name in enumerate(self.names_frame):
                    self.screen.blit(name.image, (120 + j * 560 - len(str(name.text)) * 6, 500))
        display.flip()

