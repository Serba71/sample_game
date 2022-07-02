#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from pygame import *
from block import Platform
from player import Player

WIN_WIDTH = 800 
WIN_HEIGHT = 640 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
BACKGROUND_COLOR = "#0000ff"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


def main():
    hero = Player(55,55)
    up =left = right = False 
    entities = pygame.sprite.Group() 
    platforms = [] 
    entities.add(hero)
    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-      -----            -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-    ----           --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]
    timer = pygame.time.Clock()
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("Super Mario Boy") 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) 
    bg.fill(Color(BACKGROUND_COLOR))    
    x=y=0 
    for row in level: 
        for col in row: 
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)         
            x += PLATFORM_WIDTH 
        y += PLATFORM_HEIGHT   
        x = 0                   


    while 1: 
        timer.tick(60)
        for e in pygame.event.get(): 
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == QUIT:
                raise SystemExit
        screen.blit(bg, (0,0))    
        hero.update(left, right, up, platforms)  
        entities.draw(screen) 
        pygame.display.update()     


if __name__ == "__main__":
    main()
