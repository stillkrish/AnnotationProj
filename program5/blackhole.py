# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model

class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius * 2, Black_Hole.radius * 2)
    
    def contains(self, xy):
        return self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and\
               self._y - self._height/2 <= xy[1] <= self._y + self._height/2
    def update(self, model):
        black = set()
        for i in model.find(lambda x: self.contains(x.get_location())):
            if isinstance(i, Prey):
                model.remove(i)
                black.add(i)
        return black
    def display(self, the_canvas):
        the_canvas.create_oval(self._x - self._width/2, self._y - self._height/2, self._x + self._width/2, self._y+self._height/2, fill = 'black')
