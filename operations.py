import pygame,sys
import math
from shapes import *
from pygame.locals import *
pygame.init()

    
screen = pygame.display.set_mode((340, 680))

pygame.display.set_caption("Drawing Rectangle")
pos_x = 138
pos_y = 410

piece1 = False
piece2 = False
piece3 = False
piece4 = False
piece5 = False
piece6 = False
piece7 = False

p1 = shape_1(pos_x,pos_y)
p2 = shape_2(pos_x,pos_y)
p3 = shape_3(pos_x,pos_y)
p4 = shape_4(pos_x,pos_y)
p5 = shape_5(pos_x,pos_y)
p6 = shape_6(pos_x,pos_y)
p7 = shape_7(pos_x,pos_y)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
                piece2 = piece3 = piece4 = piece5 = piece6 = piece7 = False
            elif event.key == pygame.K_2:
                piece2 = True
                piece1 = piece3 = piece4 = piece5 = piece6 = piece7 = False
            elif event.key == pygame.K_3:
                piece3 = True
                piece1 = piece2 = piece4 = piece5 = piece6 = piece7 = False
            elif event.key == pygame.K_4:
                piece4 = True
                piece1 = piece2 = piece3 = piece5 = piece6 = piece7 = False
            elif event.key == pygame.K_5:
                piece5 = True
                piece2 = piece3 = piece4 = piece1 = piece6 = piece7 = False
            elif event.key == pygame.K_6:
                piece6 = True
                piece2 = piece3 = piece4 = piece5 = piece1 = piece7 = False
            elif event.key == pygame.K_7:
                piece7 = True
                piece2 = piece3 = piece4 = piece5 = piece6 = piece1 = False
            elif event.key == pygame.K_SPACE:
                if piece1 == piece2 == piece3 == piece4 == piece5 == piece6 == piece7 == False:
                    pass
                elif piece1:
                    screen.fill((0, 200, 200))
                    p1.rotate()
                elif piece2:
                    screen.fill((0, 200, 200))
                    p2.rotate()
                elif piece3:
                    screen.fill((0, 200, 200))
                    p3.rotate()
                elif piece4:
                    pass
                elif piece5:
                    screen.fill((0, 200, 200))
                    p5.rotate()
                elif piece6:
                    screen.fill((0, 200, 200))
                    p6.rotate()
                elif piece7:
                    screen.fill((0, 200, 200))
                    p7.rotate()
            elif event.key == pygame.K_a:
                if piece1:
                    screen.fill((0, 200, 200))
                    p1.shift_left()
                if piece2:
                    screen.fill((0, 200, 200))
                    p2.shift_left()
                if piece3:
                    screen.fill((0, 200, 200))
                    p3.shift_left()
                if piece4:
                    screen.fill((0, 200, 200))
                    p4.shift_left()
                if piece5:
                    screen.fill((0, 200, 200))
                    p5.shift_left()
                if piece6:
                    screen.fill((0, 200, 200))
                    p6.shift_left()
                if piece7:
                    screen.fill((0, 200, 200))
                    p7.shift_left()
            elif event.key == pygame.K_d:
                if piece1:
                    screen.fill((0, 200, 200))
                    p1.shift_right()
                if piece2:
                    screen.fill((0, 200, 200))
                    p2.shift_right()
                if piece3:
                    screen.fill((0, 200, 200))
                    p3.shift_right()
                if piece4:
                    screen.fill((0, 200, 200))
                    p4.shift_right()
                if piece5:
                    screen.fill((0, 200, 200))
                    p5.shift_right()
                if piece6:
                    screen.fill((0, 200, 200))
                    p6.shift_right()
                if piece7:
                    screen.fill((0, 200, 200))
                    p7.shift_right()
    screen.fill((0, 200, 200))
    
    if piece1:
        screen.fill((0, 200, 200))
        p1.draw()
    if piece2:
        screen.fill((0, 200, 200))
        p2.draw()
    if piece3:
        screen.fill((0, 200, 200))
        p3.draw()
    if piece4:
        screen.fill((0, 200, 200))
        p4.draw()
    if piece5:
        screen.fill((0, 200, 200))
        p5.draw()
    if piece6:
        screen.fill((0, 200, 200))
        p6.draw()
    if piece7:
        screen.fill((0, 200, 200))
        p7.draw()

    pygame.display.update()

