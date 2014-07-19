"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 30  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 2.0  # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player): 
    """
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by making random moves, 
    alternating between players. The function should return when the game is over. 
    The modified board will contain the state of the game, so the function does not return anything.
    """
    #print "mc_trail", player
    
    movies = board.get_empty_squares()
    
    #print movies
    random.shuffle(movies)
    #print movies
    
    for mov in movies:
        board.move(mov[0], mov[1], player)
        if board.check_win() != None:
            break
        player = provided.switch_player(player)
    #print board
       
def mc_update_scores(scores, board, player): 
    """
    This function takes a grid of scores (a list of lists) with the same dimensions 
    as the Tic-Tac-Toe board, a board from a completed game, and which player 
    the machine playe= [ [0 for dummy_col in range(self.width_)] for dummy_row in range(self.height_)]r is. The function should score the completed board and 
    update the scores grid. As the function updates the scores grid directly, 
    it does not return anything
    """
    #print "mc_update_scores"  
    
    dim = board.get_dim()
    win = board.check_win()
    win_p = (win == player)
    #print board
    for row in range(dim):
        for col in range(dim):
            if win == provided.DRAW:
                pass
            elif win == None:
                print "update_score_error, game is not finished yet"
            elif board.square( row, col) == provided.EMPTY:
                pass
            elif board.square( row, col) == player:
                if win_p:
                    scores[row][col] += MCMATCH
                else:
                    scores[row][col] -= MCMATCH
            else:
                if not win_p:
                    scores[row][col] += MCOTHER
                else:
                    scores[row][col] -= MCOTHER
    #print "End update:", scores  			
     

def get_best_move(board, scores): 
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score 
    and randomly return one of them as a (row, column) tuple. 
    It is an error to call this function with a board that has no empty squares 
    (there is no possible next move), so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.
    """
    #print "get_best_move", scores
    movies = board.get_empty_squares()
    if len(movies) == 1:
        return movies[0]
        
    can = []
    for ind in range(len(movies)):
        can.append((ind, scores[movies[ind][0]][movies[ind][1]]))
    
    #print can
    can = sorted(can, key = lambda x: x[1], reverse = True)
    #print can
 
    last_ind = len(movies) -1
    for ind in range(len(can) -1):
        if can[ind+1][1] < can[0][1]:
            last_ind = ind +1
            break;
    #print last_ind
    return movies[can[random.randrange(last_ind)][0]]

     
    

def mc_move(board, player, trials): 
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. The function should use the Monte Carlo 
    simulation described above to return a move for the machine player in the 
    form of a (row, column) tuple. Be sure to use the other functions you have written!
    """
    
    scores =  [ [0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for _ in range(trials):
        brd = board.clone()
        mc_trial(brd, player)
        mc_update_scores(scores, brd, player)
    #print scores
    mov = get_best_move(board, scores)
    return mov  
    
    #movies = board.get_empty_squares()
    #return movies[0]
   


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#random.seed(3)
provided.play_game(mc_move, NTRIALS, False) 
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#random.seed(1)
#board = provided.TTTBoard(3)
#mc_trial(board, provided.PLAYERX)

 


'''
print dir(provided)
print provided.PLAYERO
print provided.PLAYERX
print provided.STRMAP
print provided.TTTBoard


['DRAW', 'EMPTY', 'PLAYERO', 'PLAYERX', 'STRMAP', 'TTTBoard', '__name__', 'play_game', 'switch_player']
3
2
{1: ' ', 2: 'X', 3: 'O'}
<class 'poc_ttt_provided.TTTBoard'>
"""

http://www.codeskulptor.org/#user34_Ptj5ZCVz5L_46.py

