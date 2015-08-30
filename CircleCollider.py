from Entity import Entity
from Renderer import Renderer
from Vector2D import Vector2D
from Physics import Physics
import Controller
import Body
CIRCLE_MASS=2000
CIRCLE_K_FRICTION=1
CIRCLE_S_FRICTION=1
def vector_shape_from_list(list):
    vector_list = []
    for item in list:
        vector_list.append(Vector2D(item[0], item[1]))
    return vector_list
CIRCLE_POINTS = [(0, 1), (1, 0), (2, 0)]
CIRCLE_POINTS_VECTOR=vector_shape_from_list(CIRCLE_POINTS)
class CircleCollide(Entity):
    def __init__(self):
        super().__init__()
        self.add_component('renderer', Renderer())
        self.add_component('physics', Physics(CIRCLE_MASS, CIRCLE_S_FRICTION, CIRCLE_K_FRICTION, Vector2D(0, 0)))
        self.add_component('body', Body.Circle(0, Vector2D(300, 300), 50, 30))
        self.add_component('controller', Controller.CircleController())
