#!/usr/bin/python

import pygame
import sys

def doit(fname, new_name, scale_x,scale_y):
    # scale is a tuple in pixels    
    img = pygame.image.load(fname)
    img = pygame.transform.scale(img, (scale_x, scale_y))
    pygame.image.save(img, new_name)
    
    
# usage
#  ./scale_image.py ball.bmp ball_20_20.bmp 20 20

if __name__ == '__main__':

    try:
        scale_x = int(sys.argv[3])
        scale_y = int(sys.argv[4])        
    except:
        print "sclae not a number"
        sys.exit();
        
    doit(sys.argv[1], sys.argv[2], scale_x, scale_y)
    




