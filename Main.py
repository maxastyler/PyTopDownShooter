import pygame
from GameController import GameController
from Player import Player
from Vector2D import Vector2D
from MouseCursor import MouseCursor

ICON_FILE = 'data/icon.png'
SCREEN_SIZE = (640, 480)
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

    game_controller = GameController()
    player = Player()
    mouse_cursor = MouseCursor()
    game_controller.add_entity(player)
    game_controller.add_entity(mouse_cursor)

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

        keys = pygame.key.get_pressed()
        mouse_btns = pygame.mouse.get_pressed()
        print(mouse_btns)
        position = Vector2D(0, 0)
        shifted = False
        if keys[pygame.K_w]:
            position+=Vector2D(0, -1)
        if keys[pygame.K_s]:
            position+=Vector2D(0, 1)
        if keys[pygame.K_a]:
            position+=Vector2D(-1, 0)
        if keys[pygame.K_d]:
            position+=Vector2D(1, 0)
        if keys[pygame.K_c]:
            shifted = True
        player.get_component('body').position+=PLAYER_SPEED*clock.get_time()*position.get_norm()
        player_to_mouse=pygame.mouse.get_pos()-player.get_component('body').position
        mouse_cursor.get_component('body').position = pygame.mouse.get_pos()
        player.get_component('body').rotation=player_to_mouse.angle_from_vector()

        #rendering
        screen.fill(BLACK)
        game_controller.render(screen)
        pygame.display.flip()


    pygame.quit()

if __name__=='__main__':
    main()
