# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:23:00 2020

@author: lenovo
learn pyGames
"""
import pygame,sys,os
from pygame.locals import *

red=[0,255,0]

#initaialize
pygame.init()

#set up window
DISPLAYSURF=pygame.display.set_mode((400,300))

pygame.display.set_caption('Slither.eat-The Snake Game')

#set up drawing surface 
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("NaagDev")
pygame.display.flip()

#a=1
while True:
#main game loop 
    for event in pygame.event.get():
        print(event)
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    

