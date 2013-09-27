#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from player import *

WIN_WIDH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDH, WIN_HEIGHT)
BACKGROUND_COLOUR = "#004400"

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"



def main():
  pygame.init()
  screen = pygame.display.set_mode(DISPLAY)
  pygame.display.set_caption("Super Mario")
  bg = Surface((WIN_WIDH, WIN_HEIGHT))

  hero = Player(55,55)
  left = right = False
  up = False
  
  
  level = [
         "-------------------------",
         "-                       -",
         "-                       -",
         "-                       -",
         "-            --         -",
         "-                       -",
         "--                      -",
         "-                       -",
         "-                   --- -",
         "-                       -",
         "-                       -",
         "-      ---              -",
         "-                       -",
         "-   -----------         -",
         "-                       -",
         "-                -      -",
         "-                   --  -",
         "-                       -",
         "-                       -",
         "-------------------------"]
  
  timer = pygame.time.Clock()
      
    
  bg.fill(Color(BACKGROUND_COLOUR)) 
  
  while 1:
    timer.tick(60)
    x=y=0 # координаты
    for row in level: # вся строка
      for col in row: # каждый символ
        if col == "-":
          pf = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
          pf.fill(Color(PLATFORM_COLOR)) 
          screen.blit(pf,(x,y))
                  
        x += PLATFORM_WIDTH 
      y += PLATFORM_HEIGHT   

      x = 0                

    hero.update(left, right, up)
    hero.draw(screen)

  
    for e in pygame.event.get():
      if e.type == QUIT:
        raise SystemExit, "QUIT"
      
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
        
    pygame.display.update()
    screen.blit(bg, (0,0))  
    
    
if __name__ == "__main__":
  main()
