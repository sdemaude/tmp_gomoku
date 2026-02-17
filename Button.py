import pygame as pg
from pygame.locals import *
from Position import Position


def create_hover_image(image, rect, factor):
    image_hover_size = (int(image.get_width() * factor), int(image.get_height() * factor))
    image_hover = pg.transform.scale(image, image_hover_size)
    return image_hover


class Button:
    def __init__(self, image_path, position: Position, size, cb, unload_on_click=True):
        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self.position = position
        pos = position.get(size)
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.callback = cb
        self.on_hover = False
        self.unload_on_click = unload_on_click
        self.image_hover = create_hover_image(self.image, self.rect, 1.2)


    def draw(self, surface):
        if self.on_hover:
            surface.blit(self.image_hover, self.position.get(self.image_hover.get_size()))
        else:
            surface.blit(self.image, self.position.get(self.image.get_size()))


    def on_button(self, pos):
        return self.rect.collidepoint(pos)


    def on_click(self):
        if self.callback:
            self.callback(self)
        if self.unload_on_click:
            self.on_hover = False

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.on_button(event.pos):
                self.on_click()
        elif event.type == MOUSEMOTION:
            if self.on_button(event.pos):
                self.on_hover = True
            else:
                self.on_hover = False


class ToggleButton(Button):
    def __init__(self, image_on_path, image_off_path, position: Position, size, initial_state=True, cb=None):
        super().__init__(image_on_path, position, size, cb)
        self.image_on = self.image
        self.image_on_hover = self.image_hover
        self.image_off = pg.transform.scale(
            pg.image.load(image_off_path).convert_alpha(), size
        )
        self.image_off_hover = create_hover_image(self.image_off, self.rect, 1.2)
        self.active = initial_state


    def on_click(self):
        self.toggle()
        if self.callback:
            self.callback(self)


    def toggle(self):
        self.active = not self.active
        self.image, self.image_hover = (self.image_on, self.image_on_hover) if self.active else (self.image_off, self.image_off_hover)