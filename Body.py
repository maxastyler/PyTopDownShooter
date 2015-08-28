class Body:
    def __init__(self, rotation, position, scale):
        self.rotation = rotation
        self.position = position
        self.scale = scale

class Circle(Body):
    def __init__(self, rotation, position, scale, radius):
        self.radius = radius
        super().__init__(rotation, position, scale)

class Polygon(Body):
    def __init__(self, rotation, position, scale, points):
        self.points = points
        super().__init__(rotation, position, scale)
