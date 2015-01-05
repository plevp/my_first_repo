#! /usr/bin/env python

import pygame

LEFT = 1

running = 1
screen = pygame.display.set_mode((320, 200))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        print "You pressed the left mouse button at (%d, %d)" % event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos

    screen.fill((0, 0, 0))
    pygame.display.flip()

