#! /usr/bin/env python
 
import pygame

screen = pygame.display.set_mode((640, 480))
running = 1
col = 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print "Quit"
        running = 0
    screen.fill((col, col, col))
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
    pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))    
    pygame.display.flip()
