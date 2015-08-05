import pygame


from life import *

def draw_life(w, h, get_next):
    pygame.init()
    w_clr = (255,255,255)
    b_clr= (0,0,0)

    cell_size = 6
    sq_sz = cell_size

    surface_w = w * cell_size
    surface_h = h * cell_size
    
    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_w, surface_h))

    my_clock = pygame.time.Clock()

    gen = get_next()
    while True:
        my_clock.tick(5)
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            print "quit"
            break;
        
        surface.fill(w_clr);
        d = gen.next();
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

draw_life(120,120, gen_life)

"""
g = gen_next1()

for j in range(100):
    print g
"""
