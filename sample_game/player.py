#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 


class Player(sprite.Sprite):
    def __init__(self, x, y):
        self.yvel = 0 
        self.onGround = False 
        sprite.Sprite.__init__(self)
        self.xvel = 0  
        self.startX = x 
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        #self.image.fill(Color(COLOR))
        self.image = image.load("player/main.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround: 
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
 
        if right:
            self.xvel = MOVE_SPEED # Право = x + n
         
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
        if not self.onGround:
            self.yvel +=  GRAVITY

        self.onGround = False; # Мы не знаем, когда мы на земле((   
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel 
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:                      
                    self.rect.right = p.rect.left 

                if xvel < 0:                      
                    self.rect.left = p.rect.right 

                if yvel > 0:                      
                    self.rect.bottom = p.rect.top 
                    self.onGround = True         
                    self.yvel = 0                 

                if yvel < 0:                     
                    self.rect.top = p.rect.bottom 
                    self.yvel = 0                