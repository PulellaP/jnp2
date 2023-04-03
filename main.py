import pygame
import os

WIDTH, HEIGHT = 1300,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JNP")


def draw_window():
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        draw_window()

    main()

if __name__ == "__main__":
    main()