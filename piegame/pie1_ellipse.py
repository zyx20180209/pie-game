import pygame,sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))
myfont = pygame.font.Font(None, 60)

white = 255,255,255
blue = 0,0,255
textImage = myfont.render("Hello Pygame", True, white)
pygame.display.set_caption("Drawing Circle")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)
    color = 255,255,0
    position = 100,150,400,200
    #   最左，最上，横轴，纵轴
    width = 10
    pygame.draw.ellipse(screen,color,position,width)

    pygame.display.update()
