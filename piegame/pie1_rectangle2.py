import pygame,sys
import random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))

pygame.display.set_caption("Drawing Rectangle")
pos_x = 0
pos_y = 0
vel_x = 1
vel_y = 0
color = 255,255,0

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    pos_x += vel_x
    pos_y += vel_y
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    if pos_x == 500 and pos_y == 0:
        vel_x = 0
        vel_y = 0.5
        color = R, G, B
        sys.exit()
    if pos_y == 400 and pos_x == 500:
        vel_y = 0
        vel_x = -1
        color = R, G, B
    if pos_x == 0 and pos_y == 400:
        vel_x = 0
        vel_y = -0.5
        color = R, G, B
    if pos_x == 0 and pos_y ==0:
        vel_y = 0
        vel_x = 1
        color = R, G, B

    
    width = 0
    pos = pos_x, pos_y, 100,100
    pygame.draw.rect(screen, color,pos,width)

    pygame.display.update()

