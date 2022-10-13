# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).

from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    hdistance = 200
    def __init__(self, x, y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self, x, y, self.radius * 2, self.radius * 2, 0, 5)
        self.randomize_angle()
    def update(self, model):
        hey = model.find(lambda x : isinstance(x,Prey) and self.distance(x.get_location()) <= Hunter.hdistance)
        if hey:
            target = sorted([(prey, self.distance(prey.get_location())) for prey in hey], key = lambda x:x[1])[0][0]
            sx,sy = target.get_location()
            x1,y1 = self.get_location()
            self.set_angle(atan2(sy-y1, sx-x1))
        Pulsator.update(self,model)
        self.move()
        return hey
        
            