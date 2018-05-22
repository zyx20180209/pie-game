import pygame,sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))

pygame.display.set_caption("Drawing Rectangle")
pos_x = 300
pos_y = 250

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    color = 227,222,0
    shade_color = 150,150,0
    bright_color = 255,255,147
    width = 0
    width_side = 6
    pos = pos_x+2, pos_y+2, 26, 26
    pygame.draw.rect(screen, color, pos, width)
    pygame.draw.line(screen, bright_color, (300,250), (330,250), 4)
    pygame.draw.line(screen, bright_color, (300,250), (300,280), 4)
    pygame.draw.line(screen, shade_color, (330,250), (330,280), 5)
    pygame.draw.line(screen, shade_color, (300,280), (330,280), 5)

    pygame.display.update()

