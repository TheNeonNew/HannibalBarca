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
        self.rectangle_draging = False
        self.taken_rect = None
        self.tr_ratio = None
        self.undo_rect = None

    def find_rect(self, engi, pos, mod="tkn"):
        """pos -> event.pos"""
        for j, rectangle in enumerate([k.rect for k in engi.details[engi.details.index(engi.start_cards)]]):
            if rectangle.collidepoint(pos):
                self.rectangle_draging = True
                if mod == "tkn":
                    self.taken_rect = rectangle
                else:
                    self.undo_rect = rectangle
                self.tr_ratio = j


    def run(self, usnms):
        """Run the main event loop."""
        eng = Engine(self.screen, usnms)
        eng.start()

        UpdateEvent = pg.USEREVENT + 0
        pg.time.set_timer(UpdateEvent, 300)
        while self.go_on:
            self.screen.fill(pg.Color('black'))
            for event in pg.event.get():
                if event.type == QUIT:
                    self.go_on = False
                
                elif event.type == pg.MOUSEBUTTONDOWN:  # if mousebutton pressed
                    if event.button == 1:  # if it's left button
                        # checking every btn
                        for j, btn in enumerate(eng.mod_buttons):
                            if btn.pressed(event.pos):  # if button pressed
                                eng.mode = eng.mode + j
                                eng.turn_level()
                                break
                        # arrow reflection and crossed  swords appearing
                        if eng.details[1].pressed(event.pos):
                            eng.up_phase()
                            eng.check_turns(pg.transform.flip(eng.details[2].image, True, False))
                            

                        if not eng.map.should_draw:
                            self.find_rect(eng, event.pos)
                    if event.button == 3: # if it's right button
                        self.find_rect(eng, event.pos, mod="undo")
                        if self.undo_rect is not None and eng.currlvlmap.which((self.undo_rect.x, self.undo_rect.y)):
                            self.undo_rect.x, self.undo_rect.y = eng.cardpos_acc[self.tr_ratio]


                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and not eng.map.should_draw:
                        self.rectangle_draging = False
                        if self.taken_rect is not None and not eng.currlvlmap.which((self.taken_rect.x, self.taken_rect.y)):
                            self.taken_rect.x, self.taken_rect.y = eng.cardpos_acc[self.tr_ratio]
                        else:
                            eng.currlvlmap.deploy(self.taken_rect)
                        self.taken_rect = None


                elif event.type == pygame.MOUSEMOTION:
                    if self.rectangle_draging and not eng.map.should_draw:
                        mouse_x, mouse_y = event.pos
                        if self.taken_rect is None:
                            continue
                        self.taken_rect.x = mouse_x
                        self.taken_rect.y = mouse_y
                        eng.update_level()

                elif event.type == UpdateEvent:
                    pass

            if eng.map.should_draw:
                # Updating level map or level depending on btn pressed
                eng.update_map()
            else:
                eng.update_level()

            pg.display.update()
        pg.quit()


game = Game()
usernames = RunMenu(pg.display.set_mode((800, 800)))
game.run(usernames)
