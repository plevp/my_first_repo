
from another_life_gui import PygameLife


glider_gun = '''
........................o...........
......................o.o...........
............oo......oo............oo
...........o...o....oo............oo
oo........o.....o...oo..............
oo........o...o.oo....o.o...........
..........o.....o.......o...........
...........o...o....................
............oo......................'''
p = PygameLife(100, 60)
p.paste(glider_gun, 8, 1)
p.run()

