from Entity import *

class Player(Entity):
    def __init__(self, health, x, y, width, height, color):
        super().__init__(health, x, y, width, height, color)
        self.velocity = 0