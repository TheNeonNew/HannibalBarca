# main
import pygame as pg
from pygame.locals import *
from menu import *
from engine import *
pygame.init()



class Game:
    """Create a single-window game with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        flags = RESIZABLE
        self.width = 800
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height), flags)

        self.go_on = True
        self.c = 1

    def run(self):
        """Run the main event loop."""
        while self.go_on:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.go_on = False
            
            self.screen.fill(pg.Color("yellow"))
            pg.display.update()
        pg.quit()


game = Game()
RunMenu(pg.display.set_mode((800, 800), RESIZABLE))
game.run()

