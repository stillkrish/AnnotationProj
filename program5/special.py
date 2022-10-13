
#A Special is a mobile simulton that moves randomly. Like a Hunter, it eats its prey but doesn't chase the closest ball/floater, instead it moves randomly
from mobilesimulton import Mobile_Simulton
from prey import Prey
import model

class Special(Mobile_Simulton):  
    radius = 10
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,self.radius * 2,self.radius * 2,0,10)
        self.randomize_angle()
        
    def update(self, model):
        black = set()
        for i in model.find(lambda x: self.contains(x.get_location())):
            if isinstance(i, Prey):
                model.remove(i)
                black.add(i)
        self.move()
        return black
    def display(self, the_canvas):
        the_canvas.create_oval(self._x - self._width/2, self._y - self._height/2, self._x + self._width/2, self._y+self._height/2, fill = 'green')