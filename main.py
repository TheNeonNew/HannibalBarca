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
        self.width = 800
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height))

        self.go_on = True
        self.c = 1

    def run(self):
        """Run the main event loop."""
        eng = Engine(self.screen)
        eng.start()
        eng.turn_level()
        UpdateEvent = pg.USEREVENT + 0
        pg.time.set_timer(UpdateEvent, 300)
        while self.go_on:
            self.screen.fill(pg.Color('black'))
            for event in pg.event.get():
                if event.type == QUIT:
                    self.go_on = False
                elif event.type == UpdateEvent:
                    pass
            eng.update_level()
            
            pg.display.update()
        pg.quit()


game = Game()
RunMenu(pg.display.set_mode((800, 800)))
game.run()

