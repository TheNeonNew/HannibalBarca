import pygame as pg
from random import shuffle
from enum import Enum

class LvlMap:
    def __init__(self):
        self.textures = {
            'PLAIN' : pg.image.load("images\\plain.png"),
            'RIVER': pg.image.load("images\\river.png"),
        }
        self.tilemap = []
        self.tilesize = 80

    def gen(self, pl):
        self.tilemap.clear()
        self.tilemap = [[self.textures['PLAIN'] for i in range(10)] for j in range(6) if 1]
        

    def draw(self, window):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                window.blit(tile, (x * self.tilesize, y * self.tilesize))

class Map:
    def __init__(self):
        self.should_draw = True
        self.objs_to_draw = [Image("images\\main_bg.jpg", (0, 0))]
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


class Line:
    def __init__(self, screen, pos, color, boldness=1):
        self.pos = pos
        self.color = color
        self.boldness = boldness
        self.sc = screen
    def draw(self):
        pg.draw.line(self.sc, pg.Color(self.color), 
                 self.pos[:2], self.pos[2:], self.boldness)
        


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
    def __init__(self, **kwargs):
        super().__init__()
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]

    def shoot(self):
        pass

class MeleeCard(BaseCard):
    """Melee units & spearmen"""
    #TODO damage <function>
    def __init__(self, **kwargs):
        super().__init__()
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
    def damage(self):
        pass

class CavalryCard(BaseCard):
    """Cavalry and elephants"""
    #TODO damage <function> as a charge <function>
    def __init__(self, **kwargs):
        super().__init__()
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
    def charge(self):
        pass

class BuffCard(BaseCard):
    """Other cards as a potion, heal and etc"""
    #TODO: apply <function> which will apply some effect to division
    def __init__(self, **kwargs):
        super().__init__()
        self.actTime = kwargs["acttime"]
    def apply(self):
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
        
