from Vector2D import Vector2D
import math
class CircleCircleCollision:
    def solve(a, b):
        penetration = None
        normal = a.position-b.position
        normal_squared = normal.norm_squared()
        radius = a.collider_radius+b.collider_radius
        if normal_squared > radius*radius:
            return penetration, normal

        distance = math.sqrt(normal_squared)
        if distance == 0:
            penetration=a.collider_radius
            normal=Vector2D(0, 0)
        else:
            penetration=radius-distance
            normal=Vector2D(normal.x/distance, normal.y/distance)
        return penetration, normal
