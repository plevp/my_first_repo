"""
Clone of 2048 game.
"""

# import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    # print "Merge:"
    # print line
    new_line = [item for item in line if item > 0]
    # print new_line
    if len(new_line) > 1:
        for idx in range(len(new_line) -1 ):
            if new_line[idx] != 0 and  new_line[idx] == new_line[idx+1]:
                new_line[idx] = 2 * new_line[idx]
                new_line[idx+1] = 0;
        # print new_line
        new_line = [item for item in new_line if item > 0]
        # print new_line
    if len(new_line) < len(line):
        new_line.extend([0] * (len(line) - len(new_line)))
    #print new_line
    return new_line
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height_ = grid_height
        self.width_ = grid_width
        self.reset()
    
    def reset(self):
        """
        # replace with your code
        """
        self.cells_ = [ [0 for dummy_col in range(self.width_)] for dummy_row in range(self.height_)]
    
    def __str__(self):
        """ 
        Return a string representation of the grid for debugging.
        """
        lines = [str(row) for row in self.cells_]
        return  '\n'.join(lines);
    

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height_
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width_
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if len(self.get_empties()) == 0:
            return
        
        # print "Move: ", direction
        if direction == LEFT:
            for line_ind in range(self.height_):
                self.cells_[line_ind] = merge(self.cells_[line_ind])
        elif direction == RIGHT:
            for line_ind in range(self.height_):
                self.cells_[line_ind] = merge(self.cells_[line_ind][::-1])[::-1]
        elif direction == UP:
            for col_ind in range(self.width_):
                tmp = [row[col_ind] for row in self.cells_] 
                tmp = merge(tmp);
                for row_ind in range(self.height_):
                    self.cells_[row_ind][col_ind] = tmp[row_ind]
                
        elif direction == DOWN:
            for col_ind in range(self.width_):
                tmp = [row[col_ind] for row in self.cells_]
                tmp = merge(tmp[::-1])
                for row_ind in range(self.height_):
                    self.cells_[row_ind][col_ind] = tmp[self.height_- row_ind -1]           
        else:
            pass

        self.new_tile()

    def get_empties(self):
        """
        Return empties cells as a list of of tupples (row, col)
        """
        empties = [];
        for col in range(self.width_):
            for row in range(self.height_):
                if self.cells_[row][col] == 0:
                    empties.append((row, col));
        return empties;

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empties = self.get_empties();
        if len(empties) > 0:
            ind = random.randint(0, len(empties) -1);
            if random.randint(1,10) == 1:
                value = 4
            else:
                value = 2
            self.set_tile_tupple(empties[ind], value)
            # print "New tile: ",  empties[ind], value
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        #print row, col
        self.cells_[row][col] = value

    def set_tile_tupple(self, tpl, value):
        """
        Set the tile at position, defined by tupple (row, col) to have the given value.
        """        
        self.cells_[tpl[0]][tpl[1]] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.cells_[row][col]

    
# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
