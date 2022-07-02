#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#ffffff"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        #self.image = image.load("world/grass.png")    
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


        