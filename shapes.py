import pygame,sys
import math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((340, 680))


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
    

class shape_1:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x, pos_y],[pos_x+34, pos_y],[pos_x+68, pos_y],[pos_x+102, pos_y]],
                     [[pos_x+34, pos_y-34],[pos_x+34, pos_y],[pos_x+34, pos_y+34],[pos_x+34, pos_y+68]],
                     [[pos_x-34, pos_y],[pos_x+34, pos_y],[pos_x, pos_y],[pos_x+68, pos_y]],
                     [[pos_x+34, pos_y-34],[pos_x+34, pos_y],[pos_x+34, pos_y+34],[pos_x+34, pos_y-68]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34

    def position(self):
        return self.list[0]


class shape_2:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x, pos_y],[pos_x, pos_y+34],[pos_x+34, pos_y+34],[pos_x+68, pos_y+34]],
                     [[pos_x+34, pos_y],[pos_x+34, pos_y+34],[pos_x+34, pos_y+68],[pos_x+68, pos_y]],
                     [[pos_x, pos_y+34],[pos_x+68, pos_y+68],[pos_x+34, pos_y+34],[pos_x+68, pos_y+34]],
                     [[pos_x, pos_y+68],[pos_x+34, pos_y],[pos_x+34, pos_y+34],[pos_x+34, pos_y+68]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34


class shape_3:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x-68, pos_y+34],[pos_x, pos_y],[pos_x-34, pos_y+34],[pos_x, pos_y+34]],
                     [[pos_x-34, pos_y],[pos_x-34, pos_y+34],[pos_x-34, pos_y+68],[pos_x, pos_y+68]],
                     [[pos_x-68, pos_y+68],[pos_x-34, pos_y+34],[pos_x-68, pos_y+34],[pos_x, pos_y+34]],
                     [[pos_x-68, pos_y],[pos_x-34, pos_y],[pos_x-34, pos_y+34],[pos_x-34, pos_y+68]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34


class shape_4:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[pos_x, pos_y+34],[pos_x, pos_y],[pos_x+34, pos_y],[pos_x+34, pos_y+34]]
                     
    def draw(self):
        draw_block(self.list[0][0], self.list[0][1])
        draw_block(self.list[1][0], self.list[1][1])
        draw_block(self.list[2][0], self.list[2][1])
        draw_block(self.list[3][0], self.list[3][1])

    def shift_left(self):
        result = True
        if self.list[0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                self.list[i][0] -= 34

    def shift_right(self):
        result = True
        if self.list[3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                self.list[i][0] += 34

                    
class shape_5:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x-34, pos_y+34],[pos_x, pos_y],[pos_x, pos_y+34],[pos_x+34, pos_y]],
                     [[pos_x-34, pos_y],[pos_x, pos_y],[pos_x-34, pos_y-34],[pos_x, pos_y+34]],
                     [[pos_x-34, pos_y],[pos_x, pos_y-34],[pos_x, pos_y],[pos_x+34, pos_y-34]],
                     [[pos_x, pos_y],[pos_x, pos_y-34],[pos_x+34, pos_y],[pos_x+34, pos_y+34]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34


class shape_6:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x-34, pos_y+34],[pos_x, pos_y],[pos_x, pos_y+34],[pos_x+34, pos_y+34]],
                     [[pos_x, pos_y],[pos_x, pos_y+34],[pos_x, pos_y+68],[pos_x+34, pos_y+34]],
                     [[pos_x-34, pos_y+34],[pos_x, pos_y+34],[pos_x, pos_y+68],[pos_x+34, pos_y+34]],
                     [[pos_x-34, pos_y+34],[pos_x, pos_y],[pos_x, pos_y+34],[pos_x, pos_y+68]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34


class shape_7:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list = [[[pos_x, pos_y],[pos_x+34, pos_y],[pos_x+34, pos_y+34],[pos_x+68, pos_y+34]],
                     [[pos_x, pos_y],[pos_x+34, pos_y],[pos_x, pos_y+34],[pos_x+34, pos_y-34]],
                     [[pos_x, pos_y-34],[pos_x+34, pos_y-34],[pos_x+34, pos_y],[pos_x+68, pos_y],],
                     [[pos_x+34, pos_y+34],[pos_x+68, pos_y],[pos_x+34, pos_y],[pos_x+68, pos_y-34]]]

    def draw(self):
        draw_block(self.list[0][0][0], self.list[0][0][1])
        draw_block(self.list[0][1][0], self.list[0][1][1])
        draw_block(self.list[0][2][0], self.list[0][2][1])
        draw_block(self.list[0][3][0], self.list[0][3][1])

    def rotate(self):
        result = True
        for i in range(4):
            if self.list[1][i][0] < 0 or self.list[1][i][0] > 340:
                result = False
        if result == True:
            a = self.list[0]
            self.list.pop(0)
            self.list.append(a)

    def shift_left(self):
        result = True
        if self.list[0][0][0] - 34 < 0:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] -= 34

    def shift_right(self):
        result = True
        if self.list[0][3][0] + 34 > 340:
            result = False
        if result == True:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j][0] += 34
