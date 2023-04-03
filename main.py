import pygame
import os

# GAME WINDOW
WIDTH, HEIGHT = 1300,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JNP")

#PLAYERS
PLAYER_BLUE_POINTS = ((20, HEIGHT/2 - 30), (20, HEIGHT/2 + 30), (100, HEIGHT/2))

# COLORS
BLUE = (0,0,255)
RED = (255,0,0)

def draw_players():
    pygame.draw.polygon(WIN, BLUE, PLAYER_BLUE_POINTS)
    pygame.draw.polygon(WIN, RED, ((1280, HEIGHT/2 - 30), (1280, HEIGHT/2 + 30), (1200, HEIGHT/2)))


def draw_window():
    draw_players()
    pygame.display.update()

def handle_input(keys_pressed):
    if keys_pressed[pygame.K_a]: # LEFT
        pass
    if keys_pressed[pygame.K_d]: # RIGHT
        pass
            


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys_pressed = pygame.key.get_pressed()
        handle_input(keys_pressed)
        draw_window()

    main()

if __name__ == "__main__":
    main()