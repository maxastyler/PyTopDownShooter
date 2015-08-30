import Body
from Vector2D import Vector2D
from Renderer import Renderer
from Physics import Physics
from Renderer import Renderer
from Entity import Entity

BULLET_MASS = 10000
BULLET_FRICTION = 4

class Bullet(Entity):
    def __init__(self, position, velocity):
        super().__init__()
        self.add_component('physics', Physics(BULLET_MASS, BULLET_FRICTION, BULLET_FRICTION, velocity))
        self.add_component('renderer', Renderer())
        self.add_component('body', Body.Circle(0, position, 1, 4))
