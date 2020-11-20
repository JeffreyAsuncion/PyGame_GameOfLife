import sys
import pygame 

BOARD_SIZE = WIDTH, HEIGHT = 640, 480
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 0, 255, 255

pygame.init()
screen = pygame.display.set_mode(BOARD_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(DEAD_COLOR)


    #screen.blit()
    pygame.display.flip()
