
import pygame
from pygame.locals import *  # Gives names like K_DOWN for key presses.
import sys
import math
import time

## my stuff 
from life import *

current_speed = 6;
tick = 0;
delta_x = 0
delta_y = 0
move_step = 5
pause_game = False
next_state = False

def move_panel(direction):
    global delta_y, delta_x
    
    if direction == K_UP:
        delta_y -= move_step
    elif direction == K_DOWN:
        delta_y += move_step
    elif direction == K_RIGHT:
        delta_x += move_step
    elif direction == K_LEFT:
        delta_x -= move_step

def handle_event(event):
    result = False;
    global current_speed, tick, pause_game, next_state
    if event.type == QUIT:
        result = True; # stop the game
    elif event.type == KEYDOWN:
        if event.key == K_MINUS  or event.key == K_KP_MINUS:  # K_KP_PLUS/MINUS on keypad
            # Slow down
            current_speed = current_speed +1;
            tick = 0;
        elif event.key == K_EQUALS or event.key == K_KP_PLUS:  # EQUALS is a PLUS
            # Speed up
            current_speed = max(1, current_speed -1);
            tick = 0;
        elif (event.key == K_DOWN or event.key == K_UP or
              event.key == K_LEFT or event.key == K_RIGHT):
            # Move
            move_panel(event.key);
        elif event.key == K_p:
            pause_game = not pause_game
        elif event.key == K_q:
            result = True
        else:
            pass
    elif event.type == KEYUP:
        if event.key == K_n and pause_game:
            next_state = True;
    else:
        pass
    return result

def get_next_state(gen):
    new_state = gen.next();
    if len(new_state) == 0:
        print "Dead!!!!"
        sys.exit()
    return new_state
    

def draw_life(w, h, cell_size, get_next):
    global tick, current_speed, next_state

    pygame.init()
    my_clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("Courier", 16)
    w_clr = (255,255,255) # white color
    b_clr= (0,0,0)        # black
    
    surface_w = w * cell_size
    surface_h = h * cell_size + 30     
    surface = pygame.display.set_mode((surface_w, surface_h))        # Create the surface of (width, height), and its window.

    gen = get_next()
    tick = current_speed;    

    while True:    
        running = True;
        
        for event in pygame.event.get():
            if handle_event(event):
                running = False;  # Quit
                break;
        if not running:
            break;

        ## speed control
        if not pause_game:
            if tick == current_speed:
                tick = 0 
                d_raw = get_next_state(gen);
            else:
                tick += 1; # just draw the same state
        else:
            if next_state:
                next_state = False
                d_raw = get_next_state(gen);
                
        my_clock.tick(30) # pygame ticks
        surface.fill(w_clr); # fill with white all space

        # print "State", st_info
        # recalculate the position
        str_info = "State: %s Center: (%d,%d)" % (state_size(d_raw), delta_x, delta_y) 
        text = myfont.render(str_info, 10, (255, 0, 0));  # text in the buttom of the window 
        surface.blit(text, ( 10, h * cell_size+5)) # show text in the buttom of the window
        surface.fill(b_clr, (0, h * cell_size, w * cell_size, 2)) # black line at the buttom for text 
        
        # put in the center (dalt_x, delta_y)
        for (i_,j_),_ in d_raw.items():
            i = i_+(w//2) + delta_x;
            j  = j_+(h//2) + delta_y
            if i < w and j < h:
                surface.fill(b_clr, (i * cell_size, j * cell_size, cell_size, cell_size))
        
        pygame.display.flip()
        
    pygame.quit()

#example for generator state
def get_next0():
    d = {}
    d[(5,5)] = 1
    yield d
    
# more examples
def get_next1():
    h = 200
    while True:
        for i in range(h -1):
            d = {};
            d[(i,i+1)] = 1
            d[(i+1,i)] = 1

            yield d
    
#draw_life(120,120, get_next1)

def doit():
    if len(sys.argv) > 1:
        read_state(sys.argv[1]);
        #read_state("examples/superfountain.cells");
    else:     
        # Infinite zig-zag
        #initial_state = [(-2,-2), (-2,-1), (-2,2), (-1,-2), (-1,1), (0,-2), (0,1), (0,2), (1,0), (2,-2), (2,0), (2,1), (2,2)]
        init0()
        
    draw_life(160 ,120, 6, gen_life)
    #draw_life(1000 ,400, 1, gen_life)

if __name__ == "__main__":
    doit()
