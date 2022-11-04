# engine for game logic
import HB_classLib as cllib
from pygame import Color


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
        #        self.start_cards = [cllib.MeleeCard("king", 5,3),
        #                           cllib.CavalryCard("horse", 3, 3),
        #                            cllib.CavalryCard("elephant", 5, 4)]
        self.start_cards = None
        self.borderline = cllib.Line(self.screen, [400, 0, 400, 480], "black", 3)
        self.blno_mans_land = [cllib.Line(self.screen, [240, 0, 240, 480], "blue", 3),
                               cllib.Line(self.screen, [560, 0, 560, 480], "red", 3)]
        self.mode = mode

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
        self.currlvlmap.draw(self.screen)
        match self.mode:
            case 1:
                self.borderline.draw()
                ratio = 1
                for name, pos in zip(self.names_frame, ((150, 500), (550, 500))):
                    self.screen.blit(name.image, (pos[0] + 5 * (len(str(name.text)) - 1) * (ratio),
                                                  pos[1]))
                    ratio = -ratio
                del ratio
            case 2:
                for el in self.blno_mans_land:
                    el.draw()
                for name, pos in zip(self.names_frame, ((120, 500), (680, 500))):
                    self.screen.blit(name.image, (pos[0] - 10 * (len(str(name.text)) - 1),
                                                  pos[1]))

