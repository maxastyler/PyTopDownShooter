from Entity import Entity
from Controller import Controller
from Renderer import Renderer
from Vector2D import Vector2D
from Physics import Physics
import math
import Body
PLAYER_MASS = 1
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
        self.add_component('controller', Controller())
        self.add_component('renderer', Renderer())
        self.add_component('body', Body.Polygon(0, Vector2D(100, 100), 10, PLAYER_SHAPE_VECTOR))
        self.add_component('physics', Physics(1))
