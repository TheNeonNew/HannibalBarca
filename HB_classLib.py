import pygame as pg

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, font=None, **kwargs):
        super(Text, self).__init__()
        self.color = color
        self.font = pygame.font.Font(font, size)
        self.kwargs = kwargs
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)

class BaseCard:
    def __init__(self):
        self.base_size = (100, 100)

    def draw(self, scr):
        #TODO: implement draw method
        pass

class RangerCard:
    """Archers and more..."""
    pass

class MeleeCard:
    """Melee units, spearmen, maybe elephants"""
    pass
        

if __name__ == "__main__":
    pass
        
