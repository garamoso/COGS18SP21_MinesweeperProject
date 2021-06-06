"""A collection of function for doing my project."""

import numpy as np
import random

def display_grid(grid, bombs, move, n):
    """Checks for any surrounding bombs for inputs given, update minefield with each new move
    
    Parameters
    ----------
    grid : numpy array
        A (n x n) matrix of all allowable moves for minesweeper
    bombs : list
        Provides all locations of bombs in grid
    move : tuple
        The row and column location for user input, from 0 - (n-1)
    n : int
        The size of the (n x n) matrix 
    
    Returns
    -------
    grid : numpy array 
        A updated (n x n) matrix of all allowable moves for minesweeper
    """
    
    bombs_near = 0

    #checks top left, top, top right, left, right, bottom left, bottom, and bottom right of input square location 
    
    if (move[0] - 1) >= 0 and (move[0] - 1) <= n - 1 and (move[1] - 1) >= 0 and (move[1] - 1) <= n - 1 and [move[0] - 1, move[1] - 1] in bombs:
        bombs_near += 1
    if move[0] >= 0 and move[0] <= n - 1 and (move[1] - 1) >= 0 and (move[1] - 1) <= n - 1 and [move[0], move[1] - 1] in bombs:
        bombs_near += 1
    if (move[0] + 1) >= 0 and (move[0] + 1) <= n - 1 and (move[1] - 1) >= 0 and (move[1] - 1) <= n - 1 and [move[0] + 1, move[1] - 1] in bombs:
        bombs_near += 1
    if (move[0] - 1) >= 0 and (move[0] - 1) <= n - 1 and move[1] >= 0 and move[1] <= n - 1 and [move[0] - 1, move[1]] in bombs:
        bombs_near += 1
    if (move[0] + 1) >= 0 and (move[0] + 1) <= n - 1 and move[1] >= 0 and move[1] <= n - 1 and [move[0] + 1, move[1]] in bombs:
        bombs_near += 1
    if (move[0] - 1) >= 0 and (move[0] - 1) <= n - 1 and (move[1] + 1) >= 0 and (move[1] + 1) <= n - 1 and [move[0] - 1, move[1] + 1] in bombs:
        bombs_near += 1
    if move[0] >= 0 and move[0] <= n - 1 and (move[1] + 1) >= 0 and (move[1] + 1) <= n - 1 and [move[0], move[1] + 1] in bombs:
        bombs_near += 1
    if (move[0] + 1) >= 0 and (move[0] + 1) <= n - 1 and (move[1] + 1) >= 0 and (move[1] + 1) <= n - 1 and [move[0] + 1, move[1] + 1] in bombs:
        bombs_near += 1
   
    grid[move[0]][move[1]] = ' ' + str(bombs_near) + ' '
    
    return grid


def check_game_status(grid, bombs, move, n):
    """Checks whether the minesweeper game is over or not
    
    Parameters
    ----------
    grid : numpy array
        A (n x n) matrix of all allowable moves for minesweeper
    bombs : list
        Provides all locations of bombs in grid
    move : tuple
        The row and column location for user input, from 0 - (n-1)
    n : int
        The size of the (n x n) matrix 
    
    Returns
    -------
    game_over : boolean
        Relays the status of current game: True means game is over, False means it should keep running   
    """
    
    game_over = None
    
    if list(move) in bombs:
        game_over = True
        print('\n')
        for loc in bombs:                    #if input is a bomb location, it reveals all the bombs location and ends the game
            grid[loc[0]][loc[1]] = ' X '
        print('\n'.join([' '.join(lst) for lst in grid]))
        print('\n')
        print('You Lose!')
    elif squares_left(grid, n) == True:
        game_over = True
        print('\n'.join([' '.join(lst) for lst in grid]))
        print('\n')
        print('You Win!')
    else:
        game_over = False
        
    return game_over


def get_inputs(grid, n):
    """Acquires inputs from user for the square they picked
    
    Parameters
    ----------
    grid : numpy array
        A (n x n) matrix of all allowable moves for minesweeper
    n : int
        The size of the (n x n) matrix
    
    Returns
    -------
    row : int
        The row selected from the user, from 0 - (n-1)
    column : int
        The column selected from the user, from 0 = (n-1)
    """
    
    valid = False
    
    if n == 5:                           #if game is a (5 x 5) grid, the following message will display to ask user input
        while(not valid):
            row = int(input('Choose row from 0-4 :\t'))
            column = int(input('Choose column from 0-4 :\t'))
            if row < 0 or row > 4 or column < 0 or column > 4 or available_square(grid, row, column):
                print('Please provide valid inputs!')
                continue
            else:
                valid = True
    elif n == 7:                        #if game is a (7 x 7) grid, the following message will display to ask user input
        while(not valid):
            row = int(input('Choose row from 0-6 :\t'))
            column = int(input('Choose column from 0-6 :\t'))
            if row < 0 or row > 6 or column < 0 or column > 6 or available_square(grid, row, column):
                print('Please provide valid inputs!')
                continue
            else:
                valid = True
    else:
        while(not valid):               #if game is a (9 x 9) grid, the following message will display to ask user input
            row = int(input('Choose row from 0-8 :\t'))
            column = int(input('Choose column from 0-8 :\t'))
            if row < 0 or row > 8 or column < 0 or column > 8 or available_square(grid, row, column):
                print('Please provide valid inputs!')
                continue
            else:
                valid = True
                
    return row, column


def available_square(grid, x, y):
    """Checks whether the user's input is open/available
    
    Parameters
    ----------
    grid : numpy array
        A (n x n) matrix of all allowable moves for minesweeper
    x : int
        The row selected from the user, from 0 - (n-1)
    y : int
        The column selected from the user, from 0 = (n-1)
    
    Returns
    -------
    is_open : boolean
        Gives status of a square's availability: returns True if square is open, False if square is not open
    """
    
    is_open = None
    
    if grid[x][y] == "' - '":
        is_open = True
    else:
        is_open = False
    
    return is_open


def squares_left(grid, n):
    """Counts and keeps track of the amount of squares that are available that are not bombs
    
    Parameters
    ----------
    grid : numpy array
        A (n x n) matrix of all allowable moves for minesweeper
    n : int
        The size of the (n x n) matrix
        
    Returns
    -------
    result : boolean
        Returns the status of open/valid squares that are not bombs. Ex: if there aren't any playable squares that are not
        bombs, result will return True
    """
    
    result = None
    counter = 0
    
    for i in range(n):                            #counting the number of squares that have not been played yet
        for j in range(n):
            if grid[i][j] == ' - ':
                counter += 1

    if counter == int((n ** 2) - (n ** 2 / 3)):  #checks if there are any available moves that are not bombs
        result = True
    else:
        result = False
    
    return result


def minesweeper():
    """Runs minesweeper's elements and interconnections
    
    Parameters
    ----------
    NOT APPLICABLE
    
    Returns
    -------
    NOT APPLICABLE
    """
    
    #sets up elements to begin a minesweeper game
    
    n = 0
    
    while(n != 5 and n != 7 and n!= 9):
        n = int(input('Choose a (n, n) grid of 5, 7, or 9! :\t'))
    
    grid = np.array([[' - '] * n for ncols in range(n)])              #creating grid
    print('\n'.join([' '.join(lst) for lst in grid]))                 #displaying starting grid
    print('\n')
    bomb_grid = np.array([[' - '] * n for ncols in range(n)])         #creating reference with randomized bomb placement
    bomb_placement = []                                               #initialize list to keep track of bomb locations
    
    while len(bomb_placement) < (n ** 2 / 3):                                  
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        if [x, y] in bomb_placement:                      #if generated bomb_placement is already taken, it generates a new one
            continue
        else:
            bomb_grid[x][y] = ' X '
            bomb_placement.append([x, y]) #adding location of bomb, will eventually refer to this when checking if user hits a bomb
    
    game_over = False
    move = None
    
    #game starts running here
    
    while (not game_over):
        move = get_inputs(grid, n)                                    #acquires move from user and checks if it is a valid one 
        grid = display_grid(grid, bomb_placement, move, n)            #updates playing grid with a valid move from user
        game_over = check_game_status(grid, bomb_placement, move, n)  #checks whether the game is over
        if game_over == False:
            print('\n'.join([' '.join(lst) for lst in grid]))         #displays grid if game is not over
        