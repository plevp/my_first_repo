#! /usr/bin/env python
 
import pygame

screen = pygame.display.set_mode((640, 400))
running = 1

col = 0
count = 0

while running:
    count += 1
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print "Quit"
        running = 0
    if count % 16 == 0:
        col = (col +1) % 255
    screen.fill((col, col, col))
    pygame.display.flip()

    
