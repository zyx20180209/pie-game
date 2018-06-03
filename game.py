import pygame,sys
import random
import time
from pygame.locals import *
from screen import *
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


def print_screen(self,screen):
    for i in range(screen.width):
        for j in range(20):
            if screen.s[i].pos(j) == True:
                draw_block(i*34 + 2, j*34 + 2)


    
screen = pygame.display.set_mode((340, 680))

pygame.display.set_caption("Drawing Rectangle")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    scr = Screen()
    starting_col = random.randint(0,2)
    starting_shape = [starting_col]
    '''
    进行操作改变横坐标
    '''
    scr._enter(starting_shape)
    while scr._over(starting_shape) == False:
        screen.fill((0, 0, 200))
        list2 = scr.print_pos()
        scr.fall_s(starting_shape)
        for i in range(len(list2)):
            draw_block(list2[i][0],list2[i][1])
        time.sleep(1)
        pygame.display.update()
    
    
    #time.sleep(0.1)
    #pygame.display.update()



    
