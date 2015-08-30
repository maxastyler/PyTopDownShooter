class Body:
    def __init__(self, rotation, position, scale, collider=True, restitution=1, render_collider=False, collider_radius=-1):
        self.rotation = rotation
        self.position = position
        self.scale = scale
        self.restitution=restitution
        self.collider=collider
        if collider_radius<0:
            self.collider_radius = self.scale
        self.render_collider = render_collider

class Circle(Body):
    def __init__(self, rotation, position, scale, radius, collider=True, restitution=0.2, render_collider=False, collider_radius=-1):
        self.radius = radius
        super().__init__(rotation, position, scale, collider, restitution, render_collider, collider_radius)

class Polygon(Body):
    def __init__(self, rotation, position, scale, points, collider=True, restitution=0.2, render_collider=False, collider_radius=-1):
        self.points = points
        super().__init__(rotation, position, scale, collider, restitution, render_collider, collider_radius)
