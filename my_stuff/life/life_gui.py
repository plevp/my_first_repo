
import pygame
from pygame.locals import *  # Gives names like K_DOWN for key presses.
import sys
import math
import time

## my stuff 
from life import *

"""
def ProcessEvent(self, event):
    # Handle a single 'event' - like a key press, mouse click, etc.
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if (event.key == K_DOWN or event.key == K_UP or
            event.key == K_LEFT or event.key == K_RIGHT):
            # Pan.
            self._world.ShiftView(event.key, max(self._width, self._height) // 20)
        elif event.key == K_MINUS or event.key == K_KP_MINUS:
            # Slow down.
            if (self._generations_per_update > 1):
                self._generations_per_update >>= 1
            else:
                self._ticks_per_update <<= 1
        elif event.key == K_EQUALS or event.key == K_KP_PLUS:
            # Speed up.
            if self._ticks_per_update > 1:
                self._ticks_per_update >>= 1
            else:
                self._generations_per_update <<= 1
        elif event.key == K_SPACE:
            # Pause.
            self._paused = not self._paused
        elif event.key == K_PAGEDOWN:
            # Zoom in.
            self._world.ZoomIn()
        elif event.key == K_PAGEUP:
            # Zoom out.
            self._world.ZoomOut()
        elif event.key == K_q and (pygame.key.get_mods() & KMOD_CTRL):
            # Quit.
            sys.exit()
"""

current_speed = 6;
tick = 0;
delta_x = 0
delta_y = 0

move_step = 5

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
    global current_speed, tick
    if event.type == pygame.QUIT:
        result = True; # stop the game
    elif event.type == pygame.KEYDOWN:
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
        else:
            pass      
    else:
        pass
    return result

def draw_life(w, h, cell_size, get_next):
    global tick, current_speed

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
        if tick == current_speed:
            tick = 0 
            d_raw = gen.next()
            if len(d_raw) == 0: # everything is dead 
                print "Dead!!!!!"
                break;
        else:
            tick += 1; # just draw the same state
            
        my_clock.tick(30)
        surface.fill(w_clr); # fill with white all space

        st_info = state_size(d_raw)
        text = myfont.render(str(st_info), 10, (255, 0, 0));
        # print "Text rect:", text.get_rect()
        surface.blit(text, ( 10, h * cell_size+5)) # show text in the buttom of the window
        surface.fill(b_clr, (0, h * cell_size, w * cell_size, 2)) # black line at the buttom for text 
        
        # print "State", st_info
        d = {}
        # recalculate the position
        # put in the center 
        for (i,j), _ in d_raw.items():
            d[(i+(w//2) + delta_x, j+(h//2) + delta_y)] = 1
            
        for (i,j),_ in d.items():
            if i < w and j < h:
                surface.fill(b_clr, (i * cell_size, j * cell_size, cell_size, cell_size))
        
        pygame.display.flip()
    pygame.quit()


def get_next0():
    d = {}
    d[(5,5)] = 1
    yield d
    
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

    print "doit"
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


"""

g = gen_next

1()

for j in range(100):
    print g
"""
