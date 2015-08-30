from Vector2D import Vector2D
from Matrix22 import Matrix22
import math
import pygame
class Renderer:
    def render(self, screen, body):
        if type(body).__name__=='Polygon':
            draw_polygon(screen, move_all_points(body.points, body.rotation, body.scale, body.position))
        if type(body).__name__=='Circle':
            pygame.draw.circle(screen, (255, 255, 255), body.position.tuple_rounded(), body.radius)
def apply_rotation(vector, rotation):
    cos=math.cos(rotation)
    sin=math.sin(rotation)
    return Matrix22(cos, sin, -sin, cos)*vector

def apply_scale(vector, scale):
    return Matrix22(scale, 0, 0, scale)*vector

def move_point(vector, rotation, scale, position):
    return position+apply_rotation(apply_scale(vector, scale), rotation)

def move_all_points(points, rotation, scale, position):
    moved_points = []
    for point in points:
        vec_point=move_point(point, rotation, scale, position)
        moved_points.append([vec_point.x, vec_point.y])
    return moved_points

def draw_polygon(screen, points):
    pygame.draw.polygon(screen, (255, 255, 255), points)
