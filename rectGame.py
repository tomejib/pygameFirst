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
    def inArea(self, point):
        return self._x <= point[0] <= self._x + self._width and self._y <= point[1] <= self._y + self._height
    
    #adds text to area
    def addText(self, text , size, color):
        font = pygame.font.SysFont(None, size)
        text_put = font.render(text, True, color) 
        self._screen.blit(text_put, (self._x + (self._width) / 4  , self._y + self._height  / 2))
       
    def __str__(self):
        return f"color + {self._color}, x : {self._x}, y : {self._y}, screen + {self._screen}, width : {self._width}, height : {self._height}, border : {self._border}"
