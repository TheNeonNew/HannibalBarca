# card mechanic implemention
from random import shuffle
import pygame as pg

# distance between some objects
def distance(cl_1, cl_2):
    if "rect" in cl_1.__dict__ and "rect" in cl_2.__dict__:
        pass

class BaseCard(pg.sprite.Sprite):
    """Parent class of all cards"""

    def __init__(self, Image_fn, pos, **kwargs):
        super().__init__()
        self.base_size = (80, 100)
        self.image = pg.transform.scale(pg.image.load(Image_fn).convert_alpha() if "png" in Image_fn else pg.image.load(Image_fn).convert(), self.base_size)
        self.image.set_colorkey(pg.Color("WHITE".lower()))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.pos = pos
        self.not_used = True
        self.yourTurn = True if not kwargs.get("urturn") else False

    def draw(self, scr):
        """Draw on screen cards"""
        if self.not_used:
            scr.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, *args):
        # screen argument must be first!!
        self.draw(args[0])

    @property
    def use(self):
        """Implementing using of card"""
        self.not_used = False
        return self.not_used


class RangerCard(BaseCard):
    """Archers and more..."""

    # TODO shoot <function> and class charasterics
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
        self.sight = 2 if not kwargs.get("sight") else kwargs.get("sight") 

    def shoot(self, other):
        if distance():
            pass


class MeleeCard(BaseCard):
    """Melee units & spearmen"""

    # TODO damage <function>
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
        self.sight = 1
        

    def damage(self, opponent):
        if self.yourTurn is True and distance(self, opponent) // 80 <= self.sight:
            opponent.health -= self.attack
            
            


class CavalryCard(BaseCard):
    """Cavalry and elephants"""

    # TODO damage <function> as a charge <function>
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]

    def charge(self):
        pass


class BuffCard(BaseCard):
    """Other cards as a potion, heal and etc"""

    # TODO: apply <function> which will apply some effect to division
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.actTime = kwargs["acttime"]
        self.effect = kwargs["effect"]

    def apply(self):
        pass


class Player:
    """Player's class """

    def __init__(self):
        self.hand = []


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
        shuffle(self.cards)



if __name__ == "__main__":
    pass
