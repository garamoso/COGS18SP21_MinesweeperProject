"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import display_grid, check_game_status, get_inputs, available_square, squares_left, minesweeper
import random
import numpy as np
##
##

def test_display_grid():
    
    assert callable(display_grid)
    
def test_check_game_status():
    
    grid = np.array([[' - '] * 5 for ncols in range(5)])  
    bombs = [[3, 3], [2, 2], [4, 1], [1, 0], [2, 0], [1, 3], [0, 3], [4, 4], [3, 2]]
    assert callable(check_game_status)
    assert isinstance(check_game_status(grid, bombs, move = (2, 2), n = 5), bool)
    assert check_game_status(grid, bombs, move = (2, 2), n = 5) == True
    
def test_get_inputs():
      
    assert callable(get_inputs)
    
def test_available_square():
    
    grid = np.array([[' - '] * 5 for ncols in range(5)])  
    grid[0][0] = "' 1 '"
    assert callable(available_square)
    assert isinstance(available_square(grid, 1, 3), bool)
    assert available_square(grid, 0, 0) == False
    
def test_squares_left():
    
    grid = np.array([[' - '] * 5 for ncols in range(5)])  
    assert callable(squares_left)
    assert isinstance(squares_left(grid, 5), bool)
    assert squares_left(grid, 5) == False
    for i in range(3):
        for j in range(3):
            grid[i][j] = ' 2 '
    assert squares_left(grid, 5) == True
    
def test_minesweeper():
    
    assert callable(minesweeper)
    



                 
    