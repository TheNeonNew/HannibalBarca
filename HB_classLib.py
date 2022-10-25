import pygame as pg
from random import shuffle
from enum import Enum

def Lvls(Enum):
    """Class for more cozy operating with levels"""
    TUTORIAL = 0
    FIRST = 1
    SECOND = 2
    LAST = 3

class Text(pygame.sprite.Sprite):
    """Text class"""
    def __init__(self, text, size, color, font=None, **kwargs):
        super(Text, self).__init__()
        self.color = color
        self.font = pygame.font.Font(font, size)
        self.kwargs = kwargs
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)

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
        
        

class RangerCard:
    """Archers and more..."""
    pass

class MeleeCard:
    """Melee units & spearmen"""
    pass

class CavalryCard:
    """Cavalry and elephants"""
    pass

class Player:
    """Player's class """
    def __init__(self):
        self.hand = []
        self.progress = Lvls.TUTORIAL

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
        
