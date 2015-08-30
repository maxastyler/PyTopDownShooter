from Entity import Entity
import Controller
from Renderer import Renderer
from Vector2D import Vector2D
from Physics import Physics
import math
import Body
PLAYER_MASS = 1000
PLAYER_STATIC_FRICTION = 0.5
PLAYER_KINETIC_FRICTION = 1
def vector_shape_from_list(list):
    vector_list = []
    for item in list:
        vector_list.append(Vector2D(item[0], item[1]))
    return vector_list
PLAYER_SHAPE=[(-1, -1), (-1, 1), (-0.5, 1), (-0.5, 0), (0.5, 0), (0.5, 1), (1, 1), (1, -1)]
PLAYER_SHAPE_VECTOR=vector_shape_from_list(PLAYER_SHAPE)

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.add_component('controller', Controller.PlayerController())
        self.add_component('renderer', Renderer())
        self.add_component('body', Body.Polygon(0, Vector2D(100, 100), 30, PLAYER_SHAPE_VECTOR))
        self.add_component('physics', Physics(PLAYER_MASS, PLAYER_STATIC_FRICTION, PLAYER_KINETIC_FRICTION, Vector2D(0, 0)))
