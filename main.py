# main
import pygame as pg
from pygame.locals import *
from menu import *
from engine import *
from enum import Enum

pygame.init()


# TODO: there is a bug with dragging another card after deploying some card

class Game:
    """Create a single-window game with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        self.width = self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height))

        self.go_on = True
        self.rectangle_draging = False
        self.taken_rect = self.tr_ratio = self.undo_rect = None

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

    def is_hasInvalidPos(self, rect_card, deployed, prevPosList):
        """Checks if card was placed on position outside the battlefield"""
        if rect_card is not None and deployed((rect_card.x, rect_card.y)) is None:
            rect_card.x, rect_card.y = prevPosList[self.tr_ratio]
            return True
        return False

    def run(self, usnms):
        """Run the main event loop."""
        eng = Engine(self.screen, usnms)
        eng.start()
        while self.go_on:
            self.screen.fill(pg.Color('black'))
            for event in pg.event.get():
                if event.type == QUIT:
                    self.go_on = False

                elif event.type == pg.MOUSEBUTTONDOWN:  # if mousebutton pressed
                    if event.button == 1:  # if it's left button
                        if any(bool_lst := [btn.pressed(event.pos) for btn in eng.mod_buttons]):
                            eng.mode = eng.mode + bool_lst.index(True)
                            eng.turn_level()
                        # arrow reflection and crossed swords appearing
                        if eng.details[1].pressed(event.pos):
                            eng.check_turns(pg.transform.flip(eng.details[2].image, True, False))

                        self.find_rect(eng, event.pos) if not eng.map.should_draw else None
                    if event.button == 3:  # if it's right button
                        self.find_rect(eng, event.pos, mod="undo")
                        self.is_hasInvalidPos(self.undo_rect, lambda *args: None,
                                              eng.cardpos_acc)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and not eng.map.should_draw:
                        if self.is_hasInvalidPos(self.taken_rect, eng.currlvlmap.which,
                                                 eng.cardpos_acc):
                            eng.currlvlmap.deploy(self.taken_rect)
                        self.rectangle_draging, self.taken_rect = False, None

                elif event.type == pygame.MOUSEMOTION:
                    if all([self.rectangle_draging, not eng.map.should_draw, self.taken_rect]):
                        self.taken_rect.x, self.taken_rect.y = event.pos
                        eng.update_level()
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
