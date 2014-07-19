"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)      
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombi in self._zombie_list:
            yield zombi
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for hum in self._human_list:
            yield hum
        return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        max_value = self.get_grid_height() * self.get_grid_width()
        self._distance_field = [[ max_value for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
        visit = poc_grid.Grid(self.get_grid_height() , self.get_grid_width())
        queue = poc_queue.Queue()
        entity_list = []
        if entity_type == HUMAN:
            entity_list = self._human_list
        else:
            entity_list = self._zombie_list
            
        for item in entity_list:
            #print item
            visit.set_full(item[0],item[1]) 
            self._distance_field[item[0]][item[1]] = 0
            queue.enqueue(item)
#        print "start with queue:", queue
#        print self.distance_field
        
        while len(queue) > 0:
            #print queue;
            item = queue.dequeue()
            #print "item", item
            neibs = self.four_neighbors(item[0], item[1])
            for nei in neibs:
                if self.is_empty(nei[0], nei[1]) and visit.is_empty(nei[0], nei[1]):
                    self._distance_field[nei[0]][nei[1]] = \
                        min(self._distance_field[nei[0]][nei[1]], \
                        self._distance_field[item[0]][item[1]]+1) 
                    queue.enqueue(nei)
                visit.set_full(nei[0], nei[1])
#            print "2:", queue 
#            ans = ""
#            for row in range(self._grid_height):
#                ans += str(self.distance_field[row])
#                ans += "\n"
#            print ans
#            print visit 
            
            
        return self._distance_field
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        #print zombie_distance
        new_humans = []
        for hum in self.humans():
            neis = self.eight_neighbors(hum[0], hum[1])
            
            maxd = zombie_distance[hum[0]][hum[1]]
            max_cells = []
            for nei in neis:
                
                if self.is_empty(nei[0], nei[1]) and zombie_distance[nei[0]][nei[1]] > maxd:
                    maxd =  zombie_distance[nei[0]][nei[1]]
            if zombie_distance[hum[0]][hum[1]] == maxd:
                max_cells.append(hum)
            for nei in neis:
                if zombie_distance[nei[0]][nei[1]] == maxd:
                    max_cells.append(nei)
            ind = random.randrange(len(max_cells))
            new_humans.append(max_cells[ind])
        self._human_list = new_humans
        #print self._human_list
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        
        #print human_distance
        new_zombies = []
        for hum in self.zombies():
            neis = self.four_neighbors(hum[0], hum[1])
            
            mind = human_distance[hum[0]][hum[1]]
            min_cells = []
            for nei in neis:
                if human_distance[nei[0]][nei[1]] < mind:
                    mind =  human_distance[nei[0]][nei[1]]
            if human_distance[hum[0]][hum[1]] == mind:
                min_cells.append(hum)
            for nei in neis:
                if human_distance[nei[0]][nei[1]] == mind:
                    min_cells.append(nei)
            ind = random.randrange(len(min_cells))
            new_zombies.append(min_cells[ind])
        self._zombie_list = new_zombies
            

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))
#p = Zombie(4,6, [(1,2), (2,2), (3,2)], [(1,1)], [(1,5), (3,3)])
#p = Zombie(30,40, None, [(1,1)], [(1,5), (3,2)])
#p.compute_distance_field(HUMAN)
#print p.compute_distance_field(HUMAN)


poc_zombie_gui.run_gui(Zombie(30, 40))
#p = Zombie(4,6, [(1,2), (2,2), (3,2)], [(1,1)], [(1,5), (3,3)])
#p = Zombie(30,40, None, [(1,1)], [(1,5), (3,2)])
#p.compute_distance_field(HUMAN)
#print p.compute_distance_field(HUMAN)




# http://www.codeskulptor.org/#user35_oqCP4uL2z4_31.py
