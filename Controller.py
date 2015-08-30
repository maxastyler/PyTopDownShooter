import pygame
from Vector2D import Vector2D

class PlayerController:
    def take_input(self,keys, mouse_input, physics):
        force_vector = Vector2D(0, 0)
        if keys[pygame.K_w]:
            force_vector+=Vector2D(0, -1)
        if keys[pygame.K_s]:
            force_vector+=Vector2D(0, 1)
        if keys[pygame.K_a]:
            force_vector+=Vector2D(-1, 0)
        if keys[pygame.K_d]:
            force_vector+=Vector2D(1, 0)
        physics.add_force(force_vector)

class CircleController:
    def take_input(self,keys, mouse_input, physics):
        force_vector = Vector2D(0, 0)
        if keys[pygame.K_UP]:
            force_vector+=Vector2D(0, -1)
        if keys[pygame.K_DOWN]:
            force_vector+=Vector2D(0, 1)
        if keys[pygame.K_LEFT]:
            force_vector+=Vector2D(-1, 0)
        if keys[pygame.K_RIGHT]:
            force_vector+=Vector2D(1, 0)
        physics.add_force(force_vector)
