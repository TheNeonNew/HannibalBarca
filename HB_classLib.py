import pygame as pg
from random import shuffle
from enum import Enum

class LvlMap:
    def __init__(self):
        self.textures = {
            'RIVER' : pg.image.load("images\\river.png"),
            'MNTIN' : pg.image.load("images\\mountain.png"),
            'PLAIN' : pg.image.load("images\\plain.png"),
            'FOREST': pg.image.load("images\\forest.png")
        }
        self.tilemap = []
        self.tilesize = 32

    def gen(self, pl):
        self.tilemap.clear()
        match pl.progress:
            case 0:
                self.tilemap.append([self.textures['RIVER']*8])
                for i in range(4):
                    self.tilemap.append([self.textures['PLAIN']*8])
                self.tilemap.append([self.textures['RIVER']*8])
        

    def draw(window):
        for row in range(len(self.tilemap) ):
            for column in range(len(self.tilemap[row]) ):
                window.blit(self.textures[self.tilemap[row][column]],
                    (column*self.tilesize, row*self.tilesize))

class Map:
    def __init__(self):
        self.should_draw = True
        self.objs_to_draw = [Image("images\\bg_MAP", (0, 0))]
    def draw(self, scr):
        if self.should_draw:
            for elem in self.objs_to_draw:
                elem.draw(scr)
    def fill_with(self, objs):
        self.objs_to_draw += objs
        
        

class Button:
    def __init__(self, pos, size, color, text, image, **kwargs):
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.image = image


class Lvls(Enum):
    """Class for more cozy operating with levels"""
    TUTORIAL = 0
    FIRST = 1
    SECOND = 2
    LAST = 3

class Text(pg.sprite.Sprite):
    """Text class"""
    def __init__(self, text, size, color, font=None, **kwargs):
        super(Text, self).__init__()
        self.color = color
        self.font = pg.font.Font(font, size)
        self.kwargs = kwargs
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)

class Image(pg.sprite.Sprite):
    """image class"""
    def __init__(self, img_fn, pos):
        self.image = pg.image.load(img_fn)
        self.pos = pos
    def draw(self, scr):
        scr.blit(self.image.get_rect(), self.pos)
        

class BaseCard(pg.sprite.Sprite):
    """Parent class of all cards"""
    def __init__(self, Image_fn, pos):
        super().__init__()
        self.base_size = (100, 100)
        self.image = pg.transform.scale(Image_fn, self.base_size)
        self.image.fill(pg.Color("WHITE".lower()))
        self.image.set_colorkey(pg.Color("WHITE".lower()))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.not_used = True


    def draw(self, scr):
        """Draw on screen cards"""
        if self.not_used:
            scr.blit(self.rect, self.pos)


    def update(self, *args):
        # screen argument must be first!!
        self.draw(args[0])

    @property
    def use():
        """Implementing using of card"""
        self.not_used = False
        return self.not_used
        
        

class RangerCard(BaseCard):
    """Archers and more..."""
    #TODO shoot <function> and class charasterics
    pass

class MeleeCard(BaseCard):
    """Melee units & spearmen"""
    #TODO damage <function>
    pass

class CavalryCard(BaseCard):
    """Cavalry and elephants"""
    #TODO damage <function> as a charge <function>
    pass

class Player:
    """Player's class """
    def __init__(self):
        self.hand = []
        self.progress = Lvls.TUTORIAL

    def upStats(self):
        if self.progress.value < 3:
            self.progress = Lvls(self.progress.value + 1)

class Hand:
    """Player's hand """
    def __init__(self):
        self.cards = []
    def fill(self, cards):
        self.cards = self.cards + [el for el in cards if 1]

class Deck:
    """Deck which contains all cards"""
    def __init__(self, all_cards):
        self.cards = all_cards
        
    def shuffle(self):
        random.shuffle(self.cards)
    
        

if __name__ == "__main__":
    pass
        
