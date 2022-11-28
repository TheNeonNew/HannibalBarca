# engine for game logic
import HB_classLib as cllib
from pygame import Color, display
import itertools as itools
from turn import Turn


class Engine:
    """Engine which will calculate gameClasses's interactions"""
    def __init__(self, screen, usnames, mode=1):
        self.names_frame = (cllib.Text(usnames[0].get_value(), 36, Color("white")),
                            cllib.Text(usnames[1].get_value(), 36, Color("white")))

        self.screen = screen

        self.mode = mode
        self.mod_buttons = [cllib.Button((260, 340), (300, 90), Color("gold"),
                                         "Divided field", None, 54, xIndF=40, yIndF=30),
                            cllib.Button((260, 450), (300, 90), Color("yellow"),
                                         "No man's land", None, 54, xIndF=20, yIndF=30)]

        self.start_cards = [cllib.MeleeCard(Image_fn="images/card1.jpg", pos=(10, 575), health=5, attack=3),
                            cllib.CavalryCard(Image_fn="images/card2.jpg", pos=(115, 575), health=3, attack=3),
                            cllib.CavalryCard(Image_fn="images/card3.png", pos=(240, 575), health=5, attack=4)]
        self.pl = cllib.Player()
        self.pl2 = cllib.Player()

        self.map = cllib.Map()
        self.currlvlmap = cllib.LvlMap()

        self.borderline = cllib.Line(self.screen, [400, 0, 400, 480], "black", 3)
        self.blno_mans_land = [cllib.Line(self.screen, [240, 0, 240, 480], "blue", 3),
                               cllib.Line(self.screen, [560, 0, 560, 480], "red", 3)]


        self.turnButton = cllib.Button((360, 485), (80, 80), Color("#E0FFFF"),
                                       "End Turn", None, 24,
                                       xIndF=5, yIndF=35, shape='round', fontColor="#800000")
        self.turnArrow = cllib.Image("images/turn_arrow.jpg", (360, 680), imSize=(90, 120))
        self.turnFight = cllib.Image("images/fight.jpg", (360, 680), imSize=(90, 120))
        self.turneng = Turn(self.pl, self.pl2, self)

        self.details = [self.currlvlmap, self.turnButton, self.turnArrow, self.start_cards]
        self.cardpos_acc = [i.pos for i in self.start_cards]

    def up_phase(self):
        """Increase phase ratio unconditionly"""
        +self.turneng

    def check_turns(self):
        self.turneng.do_logic()
        if self.turneng.phase == 2:
            self.details[2] = self.turnFight
        else:
            self.details[2] = self.turnArrow


    def genSlots(self):
        """Generating slots for cards"""
        global typlpx
        base = [10, 570, 85, 670]
        for i in range(8):
            if i >= 4:
                typlpx = 420 + (i - 4) * 95
            else:
                typlpx = base[0] + i * 95
            l1 = [typlpx, base[1], typlpx + 75, base[1]]
            l2 = [typlpx, base[1], typlpx, base[3]]
            l3 = [typlpx, base[3], typlpx + 75, base[3]]
            l4 = [typlpx + 75, base[1], typlpx + 75, base[3]]
            self.details.append(cllib.CardSlot(self.screen, [l1, l2, l3, l4],
                                               Color("white"), bn=3)
                                )

    def start(self):
        """Create default settings and init needed classes, draw map with mods buttons"""
        self.pl.hand.append(self.start_cards)
        self.map.fill_with(self.mod_buttons)
        self.map.draw(self.screen)

    def turn_level(self):
        """Turn on level, generate and draw level's map, setting up selected mode"""
        self.map.should_draw = False
        for btn in self.mod_buttons:
            btn.keepOn = False
        self.currlvlmap.gen(self.pl)
        self.currlvlmap.draw(self.screen)
        self.genSlots()

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
        self.check_turns()
        display.flip()

    def fight(self):
        pass
