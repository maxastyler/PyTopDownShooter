import pygame
import copy
from GameController import GameController
from Player import Player
from Vector2D import Vector2D
from MouseCursor import MouseCursor
from CircleCollider import CircleCollide
from Bullet import Bullet

ICON_FILE = 'data/icon.png'
SCREEN_SIZE = (900, 700)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60
PLAYER_SPEED = 0.3

def main():
    pygame.init()

    #Setting up the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('TOP DOWN SHOOTER')
    icon = pygame.image.load(ICON_FILE).convert()
    pygame.display.set_icon(icon)

    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    game_controller = GameController(SCREEN_SIZE)

    mouse_id = game_controller.add_entity(MouseCursor())
    player_id = game_controller.add_entity(Player())
    game_controller.add_entity(CircleCollide())

    bullets = []

    #main game loop
    running = True
    while running:
        clock.tick(FPS)
        #event catching
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #RUN CONTROLLER
        keys = pygame.key.get_pressed()
        mouse_btns = pygame.mouse.get_pressed()
        if mouse_btns[0]:
            add_bullet(bullets, game_controller, player_id)

        game_controller.control(keys, mouse_btns)
        game_controller.collide()
        game_controller.collide_walls()
        game_controller.apply_physics(clock.get_time())
        player_to_mouse=pygame.mouse.get_pos()-game_controller.components['body'][player_id].position
        game_controller.components['body'][mouse_id].position = Vector2D(0, 0) + pygame.mouse.get_pos()
        game_controller.components['body'][player_id].rotation=player_to_mouse.angle_from_vector()

        #rendering
        screen.fill(BLACK)
        game_controller.render(screen)
        pygame.display.flip()


    pygame.quit()

def off_screen(position):
    if position.x+50 < 0 or position.x-50 > SCREEN_SIZE[0] or position.y+50<0 or position.y-50>SCREEN_SIZE[1]:
        return True
    return False

def add_bullet(bullets, game_controller, player_id):
    bullets.append(game_controller.add_entity(Bullet(Vector2D(game_controller.components['body'][player_id].position.x, game_controller.components['body'][player_id].position.y),
    Vector2D(game_controller.components['physics'][player_id].velocity.x, game_controller.components['physics'][player_id].velocity.y))))

if __name__=='__main__':
    main()
