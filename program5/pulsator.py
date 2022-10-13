# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    meal = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 0
    def update(self, model):
        puls = Black_Hole.update(self, model)
        if puls == set():
            self.counter += 1
        else:
            self.counter = 0
            for i in puls:
                self.change_dimension(len(puls),len(puls))
        if self.counter == Pulsator.meal:
            self.change_dimension(-1,-1)
            self.counter = 0
        if self.get_dimension()[0] == 0:
            model.remove(self)
        return puls
                
            