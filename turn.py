# Turn class
from itertools import chain


class Turn:
    """This class is intended for detecting turn's changes and for promptly reacting on it
    """

    def __init__(self, plr1, plr2, eng):
        """
        phase: int (default value is 0)
        plr1: Player (field for init Player 1)
        plr2: Player (field for init Player 2)
        engine: Engine (class for manipulating interactions between objs)"""
        self.repeated = False
        self.phase = 0
        self.pl1 = plr1
        self.pl2 = plr2
        self.engine = eng

    def __pos__(self):
        """self.phase may be at only 3 states:
        phase == 0: Player 1 is making turn
        phase == 1: Player 2 is making turn
        phase == 2: There is a fight between two players' soldiers
        """
        if self.phase == 2:
            self.phase = 0
        else:
            self.phase += 1

    def return_back(self):
        """Returns all cards which survives in slots"""
        for card in chain(self.pl1.hand, self.pl2.hand):
            if card.alive:
                card.rect.x, card.rect.y = card.pos
            else:
                if card.pos[0] == 10:
                    pass
                elif card.pos[0] == 705:
                    pass



    def do_logic(self):
        """Defines player 1 or player 2 move if it's proper state for it
        Otherwise, declares that fight function must be called
        """
        match self.phase:
            case 0:
                if self.repeated:
                    self.return_back()
                    self.repeated = False
            case 2:
                self.pl1.do(self.engine.screen)
                self.pl2.do(self.engine.screen)
                self.engine.fight()
                self.repeated = True


