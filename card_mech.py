# card mechanic implemention
from random import shuffle
import pygame as pg
from HB_classLib import Image


# distance between some objects
def distance(cl_1, cl_2):
    if "rect" in cl_1.__dict__ and "rect" in cl_2.__dict__:
        return cl_2.rect.x - cl_1.rect.x, cl_2.rect.y - cl_1.rect.y


class BaseCard(pg.sprite.Sprite):
    """Parent class of all cards"""

    def __init__(self, Image_fn, pos, **kwargs):
        super().__init__()
        self.base_size = (73, 98)
        self.im = Image(Image_fn, pos, self.base_size)
        self.rect = self.im.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.pos = pos
        self.not_used = True
        self.damaged = 0

    def draw(self, scr):
        """Draw on screen cards"""
        if self.not_used:
            scr.blit(self.im.image, (self.rect.x, self.rect.y))

    def update(self, *args):
        # screen argument must be first!!
        self.draw(args[0])

    def delete(self):
        """Implementing using of card"""
        self.not_used = False
        return self.not_used

    @property
    def alive(self):
        return self.health > 0

    def damage(self, opponent):
        dist = distance(self, opponent)
        if dist[0] // 80 <= self.sight and not dist[1]:
            opponent.health -= self.attack
            self.damaged = True


class RangerCard(BaseCard):
    """Archers and more..."""

    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
        self.sight = 2 if not kwargs.get("sight") else kwargs.get("sight")



class MeleeCard(BaseCard):
    """Melee units & spearmen"""

    # TODO damage <function>
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
        self.sight = 1



class CavalryCard(BaseCard):
    """Cavalry and elephants"""

    # TODO damage <function> as a charge <function>
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.health = kwargs["health"]
        self.attack = kwargs["attack"]
        self.sight = 2

    def damage(self, other):
        dist = distance(self, other)
        if dist[0] // 80 <= self.sight and not dist[1]:
            if has_acceleration := hasattr(self, "acceleration"):
                self.rect.x += self.acceleration * 20
            elif not has_acceleration and self.pos[0] <= 400:
                self.acceleleration = 1
            else:
                self.acceleleration = 0

            other.health -= self.attack
            self.damaged = True


class BuffCard(BaseCard):
    """Other cards as a potion, heal and etc"""

    # TODO: apply <function> which will apply some effect to division
    def __init__(self, Image_fn, pos, *args, **kwargs):
        super().__init__(Image_fn, pos)
        self.actTime = kwargs["acttime"]
        self.effect = kwargs["effect"]

    def apply(self):
        if card.rect.x // 80 == self.rect.x // 80:
            # TODO: make effect
            pass


class Player:
    """Player's class """

    def __init__(self):
        self.hand = Hand()

    def do(self, scr):
        for card in self.hand:
            card.update(scr)



class Hand:
    """Player's hand """

    def __init__(self):
        self.cards = []
        self.index = 0

    def fill(self, cards):
        self.cards = self.cards + [el for el in cards if 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.cards):
            self.index = 0
            raise StopIteration
        else:
            res = self.cards[self.index]
            self.index += 1
            return res


class Deck:
    """Deck which contains all cards"""

    def __init__(self, all_cards):
        self.cards = all_cards

    def shuffle(self):
        shuffle(self.cards)


if __name__ == "__main__":
    pass
