
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
        elif event.key == K_EQUALS or event.key == K_KP_PLUS:
            # Speed up
            current_speed = max(1, current_speed -1);
            tick = 0;
        else:
            #print event.type, K_PLUS, K_EQUALS, K_KP_PLUS
            pass
        
    else:
        pass
    return result


        

def draw_life(w, h, get_next):
    pygame.init()

    w_clr = (255,255,255) # white color
    b_clr= (0,0,0)        # black 

    cell_size = 6
    sq_sz = cell_size

    surface_w = w * cell_size
    surface_h = h * cell_size + 30 
    
    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_w, surface_h))

    my_clock = pygame.time.Clock()


    global tick, current_speed


    gen = get_next()
    tick = current_speed;
        
    myfont = pygame.font.SysFont("Courier", 16)

    while True:
        
        # Look for an event from keyboard, mouse, etc.
        # ev = pygame.event.poll() # take only one event

        running = True;
        for event in pygame.event.get():
            if handle_event(event):
                running = False;
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
        for (i,j), _ in d_raw.items():
            d[(i+(w//2), j+(h//2))] = 1
            
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
        
    draw_life(160 ,120, gen_life)




if __name__ == "__main__":
    doit()


"""

g = gen_next

1()

for j in range(100):
    print g
"""
