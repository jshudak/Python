"""
Course: Introduction to Python Programming
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Jeffrey Hudak'
#%%
import random
import copy

# %%
def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board    
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    print(' ', Board[0][0], '|', Board[0][1], '|', Board[0][2], 
          '\n -----------\n ',
          Board[1][0], '|', Board[1][1], '|', Board[1][2], 
          '\n -----------\n ',
          Board[2][0], '|', Board[2][1], '|', Board[2][2], '\n ')
    
    
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        return True  if Board[i][j] is empty ' '
        return False if Board[i][j] is not empty
        return False if i or j is invalid (e.g. i = -1 or 100)
    '''
    if i > 2 or j > 2 or 0 > i or 0 > j or Board[i][j] != ' ':
        return False
    
    return True
    
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameters: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    counter = 0
    
    for i in range(0, 3):
        for j in range(0, 3):
            if Board[i][j] != ' ':
                counter += 1
                
    return counter
    
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if(GetNumberOfChessPieces(Board) == 9):
        return True
    
    return False


#%%
def IsBoardEmpy(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if(GetNumberOfChessPieces(Board)):
        return False
    
    return True
    
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag
    '''
    Board[Choice[0]][Choice[1]] = Tag
    
    
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters:        
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    while True:
        try:
            row = int(input('Choose a row to place an ' + Tag + ' with order 0 as the top, 2 as the bottom: '))
        except:
            print('Invalid input. Must be 0, 1, or 2.')
            continue
        
        try:
            col = int(input('Now choose which column to place ' + Tag + ' with order 0 | 1 | 2  : '))
        except:
            print('Invalid input. Must be 0, 1, or 2.')
            continue
        
        
        if not IsSpaceFree(Board, row, col):
            print('Invalid location. Try another free spot between 0 and 2.')
            continue
        else:
            break
    
    return(row, col)


#%%
def ComputerPlayer(Tag, Board):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if it is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    
    while(True):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if IsSpaceFree(Board, row, col):
            return (row, col)
            
        


#%%
def Judge(Board):
    '''
    Parameters:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
                i.e. if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    
    winner = 0
            
    items = GetNumberOfChessPieces(Board)
    
    if items < 5:
        return 0
            
    matches = [[0, 1, 2], [3, 4, 5], 
               [6, 7, 8], [0, 3, 6], 
               [1, 4, 7], [2, 5, 8], 
               [0, 4, 8], [2, 4, 6]] 
  
    
    for i in range(8):
        refChar = Board[matches[i][0]]
        if refChar == ' ':
            continue
        
        elif (Board[matches[i][0]] == refChar) and (Board[matches[i][1]] == refChar) and (Board[matches[i][2]] == refChar):
            winner = refChar
            break
        
    if winner == 'X':
        winner = 1
    elif winner == 'O':
        winner = 2
    elif winner == 0 and GetNumberOfChessPieces(Board)  == 9:
        winner = 3
        
    return winner

        
#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    if(Outcome == 0):
        print('The game continues!')
    elif(Outcome == 1):
        print(NameX, 'has won the game!')
    elif(Outcome == 2):
        print(NameO, 'has won the game!')
    elif(Outcome == 3):
        print('The game as ended as most do, in a tie.')
        
        
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.  
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer        
        PlayerO = HumanPlayer     
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer        
        PlayerX = HumanPlayer   
        
    return PlayerX, PlayerO


#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    
    # determine the order of the players
    PlayerX, PlayerO = Which_Player_goes_first()
    
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    while True:
        
        # (1)  get the choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
        if(NameX == 'HumanPlayer'):
            choice = HumanPlayer('X', Board)
        else:
            choice = ComputerPlayer('X', Board)
            
        # (2)  update the Board
        UpdateBoard(Board, 'X', choice)
        
        # (3)  draw the Board
        DrawBoard(Board)
        
        # (4)  get the outcome from Judge
        winner = Judge(Board)
        
        # (5)  show the outcome
        ShowOutcome(winner, NameX, NameO)
        
        # (6)  if the game is completed (win or tie), then break the loop
        if winner != 0:
            break
        
        # (7)  get the choice from PlayerO
        if(NameO == 'HumanPlayer'):
            choice = HumanPlayer('O', Board)
        else:
            choice = ComputerPlayer('O', Board)
            
        # (8)  update the Board
        UpdateBoard(Board, 'O', choice)
        
        # (9)  draw the Board
        DrawBoard(Board)
        
        # (10)  get the outcome from Judge
        winner = Judge(Board)
        
        # (11)  show the outcome
        ShowOutcome(winner, NameX, NameO)
        
        # (12)  if the game is completed (win or tie), then break the loop
        if winner != 0:
            break
    #---------------------------------------------------
    # your code starts from here
    # obviously my code is above and I used the comments as a guide
    
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver\nBy", author())
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
