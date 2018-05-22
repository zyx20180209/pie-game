import pygame,sys
import random
import time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption("Drawing Rectangle")
pos_x = 0
pos_y = 0
vel_x = 0
vel_y = 30
color = 255,255,0
box0 = [600]
box1 = [600]

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    pos_x += vel_x
    pos_y += vel_y
      
    if pos_x == 0 and pos_y == box0[-1]-30:
        box0 += [pos_y]
        a = random.randint(0,1)
        pos_x = 30 * a
        pos_y = 0
        
    if pos_x == 30 and pos_y == box1[-1]-30:
        box1 += [pos_y]
        a = random.randint(0,1)
        pos_x = 30 * a
        pos_y = 0
    
    width = 0
    pos = pos_x, pos_y, 30, 30
    pygame.draw.rect(screen,color,pos,width)

    if box0 != []:
        for i in range(len(box0)):
            pos_b0 = 0, box0[i], 30, 30
            pygame.draw.rect(screen,color,pos_b0,width)
                        
    if box1 != []:
        for i in range(len(box1)):
            pos_b1 = 30, box1[i], 30, 30
            pygame.draw.rect(screen,color,pos_b1,width)
    
    time.sleep(0.1)
    pygame.display.update()

    if box0[-1] == 0 or box1[-1] == 0:
        sys.exit()

