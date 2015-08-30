from Vector2D import Vector2D
from Entity import Entity
from Renderer import Renderer
import Body
class MouseCursor(Entity):
    def __init__(self):
        super().__init__()
        self.add_component('body', Body.Circle(0, (0, 0), 0, 3, False))
        self.add_component('renderer', Renderer())
