import pygame
from pygame.constants import KEYUP, MOUSEBUTTONDOWN, MOUSEMOTION, QUIT, \
                             K_p, K_q, K_s, K_ESCAPE, K_SPACE


from another_life import Life

import time

class PygameLife(Life):
    def __init__(self, width, height,
                 background=pygame.Color(240, 240, 255),
                 foreground=pygame.Color('black'),
                 cell_size=4):
        super(PygameLife, self).__init__(width, height)
        self.background = background
        self.foreground = foreground
        self.cell_size = cell_size

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(self.background)
        c = self.cell_size
        for x in range(self.width):
            for y in range(self.height):
                if self.live[self.cell(x, y)]:
                    screen.fill(self.foreground, pygame.Rect(x * c, y * c, c, c))
        pygame.display.flip()
        #pygame.time.Clock().tick(30)

    def screen_cell(self, pos):
        """Return the cell number corresponding to screen position 'pos', or
        None if the position is out of bounds.

        """
        x, y = pos
        x //= self.cell_size
        y //= self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cell(x, y)
        return None

    def run(self):
        pygame.init()
        pygame.display.set_mode((self.width * self.cell_size,
                                 self.height * self.cell_size))
        paused = False
        drawing = False
        running = True
        while running:
            for event in pygame.event.get():
                t = event.type
                if t == QUIT or t == KEYUP and event.key in (K_q, K_ESCAPE):
                    running = False
                elif t == KEYUP and event.key in (K_p, K_SPACE):
                    paused = not paused
                elif t == KEYUP and event.key in (K_s,):
                    self.update()
                elif t == MOUSEBUTTONDOWN and event.button == 1:
                    paused = True
                    p = self.screen_cell(event.pos)
                    drawing = not self.live[p]
                    self.set(p, drawing)
                elif t == MOUSEMOTION and event.buttons[0]:
                    paused = True
                    self.set(self.screen_cell(event.pos), drawing)
            if paused:
                pygame.display.set_caption('Paused (press SPACE to run)')
            else:
                pygame.display.set_caption('Life')
                self.update()
            self.draw()
        pygame.quit()
    
