import pygame as pg


class LvlMap:
    def __init__(self):
        self.textures = {
            'PLAIN': pg.image.load("images\\plain.png"),
            'RIVER': pg.image.load("images\\river.png"),
        }
        self.tilemap = []
        self.tilesize = 80
        self.deployed_cards = []

    def gen(self):
        self.tilemap.clear()
        self.tilemap = [[self.textures['PLAIN'] for i in range(10)] for j in range(6) if 1]

    def draw(self, window):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                window.blit(tile, (x * self.tilesize, y * self.tilesize))

    def set(self, scr):
        self.gen()
        self.draw(scr)

    @staticmethod
    def which(crds):
        if crds[1] in range(481):
            tile_x = (crds[0] // 80) + 1
            tile_y = (crds[1] // 80) + 1
            return tile_x, tile_y
        else:
            return None

    def deploy(self, card):
        self.deployed_cards.append(card)

    def undo(self, card):
        if card in self.deployed_cards:
            self.deployed_cards.remove(card)


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
    def __init__(self, pos, size, color, text, font, fontSize, **kwargs):
        self.btntext = None
        self.pos = pos
        self.size = size
        self.color = color

        self.text = text
        self.font = pg.font.Font(font, fontSize)
        self.fontSize = fontSize
        self.fontColor = "black" if not kwargs.get("fontColor") else kwargs.get("fontColor")

        self.rect = pg.Rect(self.pos[0], self.pos[1],
                            self.size[0],
                            self.size[1])
        self.x_indentFactor = kwargs["xIndF"]  # value indicating the text indent from the button along the x-axis
        self.y_indentFactor = kwargs['yIndF']  # value indicating the text indent from the button along the y-axis
        self.keepOn = True
        self.shape = kwargs.get("shape")

    def pressed(self, crds):
        if self.rect.collidepoint(crds) and self.keepOn:
            return True
        return False

    def draw(self, surface):
        if self.shape is None:
            pg.draw.rect(surface, self.color, self.rect)
        elif self.shape == 'round':
            pg.draw.circle(surface, self.color, self.rect.center, self.size[0] / 2)
        self.btntext = Text(str(self.text), self.fontSize, pg.Color(self.fontColor))
        surface.blit(self.btntext.image, (self.pos[0] + self.x_indentFactor, self.pos[1] + self.y_indentFactor))


class Line:
    def __init__(self, screen, pos, color, boldness=1):
        self.pos = pos
        self.color = color
        self.boldness = boldness
        self.sc = screen

    def draw(self):
        pg.draw.line(self.sc, pg.Color(self.color),
                     self.pos[:2], self.pos[2:], self.boldness)


class CardSlot:
    def __init__(self, scr, ps_slot_lst, color, bn=1):
        self.topline = Line(scr, ps_slot_lst[0], color, boldness=bn)
        self.bottomline = Line(scr, ps_slot_lst[1], color, boldness=bn)
        self.leftline = Line(scr, ps_slot_lst[2], color, boldness=bn)
        self.rightline = Line(scr, ps_slot_lst[3], color, boldness=bn)

    def draw(self, *args):
        for elem in self.__dict__:
            if "line" in elem:
                self.__dict__.get(elem).draw()


class Text(pg.sprite.Sprite):
    """Text class"""

    def __init__(self, text, size, color, font=None, **kwargs):
        super(Text, self).__init__()
        self.rect = None
        self.image = None
        self.color = color
        self.font = pg.font.Font(font, size)
        self.kwargs = kwargs
        self.text = text
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)


class Image(pg.sprite.Sprite):
    """image class"""

    def __init__(self, img_fn, pos, imSize=(800, 800)):
        super().__init__()
        if isinstance(img_fn, str):
            self.image = pg.transform.scale(pg.image.load(img_fn).convert_alpha().convert(), imSize)
            if "rom" in img_fn or "kar" in img_fn:
                self.image.set_colorkey([0, 0, 0])
        else:
            self.image = img_fn
        self.image.set_colorkey([255, 255, 255])
        self.pos = pos

    def draw(self, scr):
        scr.blit(self.image, self.pos)


if __name__ == "__main__":
    pass
