import sys, pygame
import time


pygame.init()

size = width, height = 640, 480
black = 0, 0, 0
speed = [2,2]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

print ball
print ballrect


print pygame.sound

while 1:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)   # or     screen.blit(ball, (ballrect[0], ballrect[1]))
    pygame.display.flip()



#time.sleep(2)


