#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35

class Player(sprite.Sprite):
  def __init__ (self,x,y):
    sprite.Sprite.__init__(self)
    self.xvel = 0
    self.startX = x
    
    self.startY = y
    self.image = Surface((WIDTH,HEIGHT))
    self.image.fill(Color(COLOR))
    self.rect = Rect(x,y, WIDTH, HEIGHT)
    
    self.yvel = 0
    self.onGround = False
    
  def update(self, left, right, up):
    if up:
      if self.onGround:
        self.yvel = -JUMP_POWER    
    
    if left:
      self.xvel = -MOVE_SPEED
      
    if right:
      self.xvel = MOVE_SPEED
      
    if not(left or right):
        self.xvel = 0
    
    if not self.onGround:
      self.yvel += GRAVITY
    
    self.onGround = False
    self.rect.y += self.yvel  
    
    self.rect.x += self.xvel
    
  def draw (self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
