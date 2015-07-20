from itertools import product


class Life(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        cells = (width + 2) * (height + 2)
        self.live = [False] * cells
        self.in_bounds = [True] * cells
        self.neighbours = [0] * cells
        for i in range(width + 2):
            self.in_bounds[i] = self.in_bounds[-i] = False
        for j in range(height):
            k = (j + 1) * (width + 2)
            self.in_bounds[k - 1] = self.in_bounds[k] = False
        self.neighbourhood = [y * (width + 2) + x
                              for x, y in product((-1, 0, 1), repeat=2)
                              if x or y]
        self.needs_update = set()

    def cell(self, x, y):
        """Return the cell number corresponding to the coordinates (x, y)."""
        return (self.width + 2) * (y + 1) + x + 1

    def set(self, p, value):
        """Set cell number 'p' to 'value' (True=live, False=dead)."""
        if value != self.live[p] and self.in_bounds[p]:
            self.live[p] = value
            self.needs_update.add(p)
            adjust = 1 if value else -1
            for n in self.neighbourhood:
                n += p
                if self.in_bounds[n]:
                    self.neighbours[n] += adjust
                    self.needs_update.add(n)

    def update(self, steps=1):
        """Update the world by 'steps' generations (default: 1)."""
        for _ in range(steps):
            u = [(p, self.live[p], self.neighbours[p]) for p in self.needs_update]
            self.needs_update = set()
            for p, live, neighbours in u:
                if live and not 2 <= neighbours <= 3:
                    self.set(p, False)
                elif not live and neighbours == 3:
                    self.set(p, True)

    def paste(self, s, x, y):
        """Decode 's' as a life pattern (o = live, any other character = dead)
        and paste it with top left corner at (x, y).

        """
        for j, line in enumerate(s.strip().splitlines()):
            for i, char in enumerate(line.strip()):
                self.set(self.cell(x + i, y + j), char == 'o')

