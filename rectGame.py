from shapeGame import shape
import pygame


class Rect(shape):

    _height = 0  # hight rectangle
    _width = 0  # width rectangle
    _screen = None  # screen
    _border = 0  # border of shape

    def __init__(self, color, x, y, screen, width, height, border):

        super().__init__(color,  x, y)
        self._width = width
        self._height = height
        self._screen = screen
        self._border = border

    # drwaing rectangle
    def draw(self):
        pygame.draw.rect(self._screen, self._color, [
                         self._x, self._y, self._width, self._height],  self._border)

    def _height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_screen(self):
        return self._screen

    def get_border(self):
        return self._border

    # is value in
    def inArea(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
