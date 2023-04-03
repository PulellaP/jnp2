import pygame
import os

# GAME WINDOW
WIDTH, HEIGHT = 1300,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JNP")

# COLORS
BLUE = (0,0,255)
RED = (255,0,0)

#PLAYER INFO
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 100

LEFT_PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'impossible-triangle.png'))
LEFT_PLAYER = pygame.transform.rotate(pygame.transform.scale(
    LEFT_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270)




def draw_window(left_player):
    WIN.blit(LEFT_PLAYER, (left_player.x, left_player.y))
    pygame.display.update()

def handle_input(keys_pressed):
    if keys_pressed[pygame.K_a]: # LEFT
        pass
    if keys_pressed[pygame.K_d]: # RIGHT
        pass
            


def main():
    left_player = pygame.Rect(100, 350, PLAYER_WIDTH, PLAYER_WIDTH)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        # keys_pressed = pygame.key.get_pressed()
        # handle_input(keys_pressed)
        draw_window(left_player)

    main()

if __name__ == "__main__":
    main()