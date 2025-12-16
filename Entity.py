class Entity:

    def __init__(self, health, x, y, width, height, color):
        self.health = health
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y