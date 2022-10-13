# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self,x,y,Floater.radius * 2, Floater.radius * 2, 0, 5)
        self.randomize_angle()
    def update(self, model):
        if random() <= 0.3:
            speed = random() - 0.5
            angle = random() - 0.5
            while self.get_speed() + speed < 3 or self.get_speed() + speed > 7:
                speed = random() - 0.5
            self.set_velocity(self.get_speed() + speed, self.get_angle() + angle)
        self.move()
        self.wall_bounce()
    def display(self, the_canvas):
        the_canvas.create_oval(self._x - Floater.radius, self._y-Floater.radius, self._x+Floater.radius, self._y+Floater.radius, fill = "red")
