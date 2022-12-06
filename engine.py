# engine for game logic
import HB_classLib as cllib
from card_mech import *
from pygame import Color, display
import itertools as itools
from turn import Turn


def genSlots(details, screen):
    """Generating slots for cards"""
    base = [10, 570, 85, 670]
    for i in range(8):
        typlpx = 420 + (i - 4) * 95 if i >= 4 else base[0] + i * 95
        l1 = [typlpx, base[1], typlpx + 75, base[1]]
        l2 = [typlpx, base[1], typlpx, base[3]]
        l3 = [typlpx, base[3], typlpx + 75, base[3]]
        l4 = [typlpx + 75, base[1], typlpx + 75, base[3]]
        details.append(cllib.CardSlot(screen, [l1, l2, l3, l4],
                                      Color("white"), bn=3))


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

        self.start_cards = [MeleeCard(Image_fn="images/card1.jpg", pos=(10, 575), health=5, attack=3),
                            CavalryCard(Image_fn="images/card2.xcf", pos=(108, 575), health=3, attack=3),
                            CavalryCard(Image_fn="images/card3.xcf", pos=(198, 575), health=5, attack=4)]
        self.pl = Player()
        self.pl2 = Player()

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

    def check_turns(self, transformed, is_increase=True):
        self.up_phase() if is_increase else None
        self.turneng.do_logic()
        match self.turneng.phase:
            case 0:
                self.details[2] = cllib.Image(self.turnArrow.image,
                                              (360, 680), imSize=(90, 120)
                                              )

            case 1:
                self.details[2] = cllib.Image(transformed,
                                              (360, 680), imSize=(90, 120))
            case 2:
                self.details[2] = cllib.Image(self.turnFight.image,
                                              (360, 680), imSize=(90, 120)
                                              )

    def start(self):
        """Create default settings and init needed classes, draw map with mods buttons"""
        self.pl.hand.fill([self.start_cards[0], self.start_cards[1]])
        self.pl2.hand.fill([self.start_cards[2]])
        self.map.fill_with(self.mod_buttons)
        self.map.draw(self.screen)

    def turn_level(self):
        """Turn on level, generate and draw level's map, setting up selected mode"""
        self.map.should_draw = False
        for btn in self.mod_buttons:
            btn.keepOn = False
        self.currlvlmap.set(self.screen)
        genSlots(self.details, self.screen)

    def update_map(self):
        self.map.draw(self.screen)

    def update_level(self):
        nested = lambda b: b is self.start_cards or isinstance(b, list | tuple)
        for det in self.details:
            det.draw(self.screen) if not nested(det) else [atom.draw(self.screen) for atom in det]
        blitter = lambda align, factor: (
            self.screen.blit(name.image, (align + index * factor - len(str(name.text)) * 6, 500))
            for index, name in enumerate(self.names_frame)
        )
        match self.mode:
            case 1:
                self.borderline.draw()
                blitter(200, 400)
            case 2:
                for el in self.blno_mans_land: el.draw()
                blitter(120, 560)
        display.flip()

    def fight(self):
        pass
