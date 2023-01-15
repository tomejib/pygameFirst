from abc import ABC, abstractmethod
# abstarkt class shape


class shape(ABC):
    _x = 0  # x place
    _y = 0  # y place
    _screen = None #screen place
    _color = "black"
    @abstractmethod
    def __init__(self, color , x, y ):
        self._x = x
        self.y = y
        self._color = color
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    
    def __str__(self):
        return f"x : {self.x}, y : {self.y}, in screen: {self.screen}"
    

