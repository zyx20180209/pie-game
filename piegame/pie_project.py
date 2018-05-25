import pygame,sys
import random
import time
from pygame.locals import *
pygame.init()


def draw_block(pos_x, pos_y):
    color = 227,222,0
    shade_color = 150,150,0
    bright_color = 255,255,147
    width = 0
    width_side = 6
    pos = pos_x+2, pos_y+2, 26, 26
    pygame.draw.rect(screen, color, pos, width)
    pygame.draw.line(screen, bright_color, (pos_x,pos_y), (pos_x + 30,pos_y), 4)
    pygame.draw.line(screen, bright_color, (pos_x,pos_y), (pos_x,pos_y + 30), 4)
    pygame.draw.line(screen, shade_color, (pos_x + 30,pos_y), (pos_x + 30,pos_y+30), 5)
    pygame.draw.line(screen, shade_color, (pos_x,pos_y + 30), (pos_x + 30,pos_y+30), 5)

    
screen = pygame.display.set_mode((340, 680))

pygame.display.set_caption("Drawing Rectangle")
pos_x = 0
pos_y = 0
vel_x = 0
vel_y = 34
color = 255,255,0
box0 = [680]
box1 = [680]

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    pos_x += vel_x
    pos_y += vel_y
      
    if pos_x == 0 and pos_y == box0[-1]-34:
        box0 += [box0[-1]-34]
        a = random.randint(0,1)
        pos_x = 34 * a
        pos_y = 0
        
    if pos_x == 34 and pos_y == box1[-1]-34:
        box1 += [box1[-1]-34]
        a = random.randint(0,1)
        pos_x = 34 * a
        pos_y = 0
    
    width = 0
    pos = pos_x, pos_y, 30, 30
    draw_block(pos_x, pos_y)
    if box0 != []:
        for i in range(len(box0)):
            draw_block(0, box0[i])
                        
    if box1 != []:
        for i in range(len(box1)):
            draw_block(34, box1[i])
    
    time.sleep(0.1)
    pygame.display.update()

    if box0[-1] == 0 or box1[-1] == 0:
        sys.exit()



    
