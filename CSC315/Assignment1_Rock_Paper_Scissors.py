"""
Course: Introduction to Python Programming
Student Name:
"""
#%% 
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    
    print("~~ Rock Paper Scicors, the Python Program! ~~")
    print("Please type one of the following options:")
    print('- (g) to see the statistics of your current session')
    print('- (q) to quit the game')
    print('- Your choice of (r)ock, (p)aper, or (s)cisors')
    
    valid = ['R', 'P', 'S', 'Q', 'G']
    choice = ''
    tries = 0
    
    while(choice not in valid):
       if(tries != 0):
            print(choice, 'is not a valid input.')
            
       choice = str(input("Type your choice: ")).upper()
       tries += 1
       
    if(choice == 'R'):
        choice = 'Rock'
    elif(choice == 'S'):
        choice = 'Scissors'
    elif(choice == 'P'):
        choice = ('Paper')
    elif(choice == 'G'):
        PrintGameRecord(GameRecord)
        
    print()
    return choice
    

# %%
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    
    rng = randint(0, 8)
    
    if((int)(rng/3) == 0):
        return 'Rock'
    
    elif((int)(rng/3) == 1):
        return 'Paper'
    
    elif((int)(rng/3) == 2):
        return 'Scissors'
    
# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    
    output = 0
    
    if(ChoiceOfComputerPlayer == ChoiceOfHumanPlayer):
        return output
    elif(ChoiceOfComputerPlayer == 'Rock'):
        if(ChoiceOfHumanPlayer == 'Paper'):
            output = 2
        else:
            output = 1
            
    elif(ChoiceOfComputerPlayer == 'Paper'):
        if(ChoiceOfHumanPlayer == 'Scissors'):
            output = 2
        else:
            output = 1
            
    elif(ChoiceOfComputerPlayer == 'Scissors'):
        if(ChoiceOfHumanPlayer == 'Rock'):
            output = 2
        else:
            output = 1
    
    return output

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    print('--------------------------------------------------------------')
    print('You chose', ChoiceOfHumanPlayer, 'and the Computer decided on', ChoiceOfComputerPlayer, '...')
    if(Outcome == 0):
        print('Both players thought the same thing >>> Tie <<<')
        
    elif(Outcome == 1):
        print('The Computer seeminlgly read your mind >>> Computer Wins <<<')
        
    else:
        print('You beat the Computer with a lucky guess >>> You win <<<')
    print('--------------------------------------------------------------')
    print('\n')
        
# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
    
    return

# %%
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    
    print('----- Record of Games -----')
    print('Number of rounds', len(GameRecord[2]))
    print('You have won', GameRecord[2].count(2), 'times')
    print('The computer has won', GameRecord[2].count(1), 'times')
    print('   You   \t|\t   CPU   ')
    
    rounds = len(GameRecord[2])
    i = 0
    while(i < rounds):
        print(GameRecord[0][i], '\tvs\t', GameRecord[1][i])
        i += 1
        
    print()
    
# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    
    humanList = []
    cpuList = []
    outcomeList = []
    gameRecord = [humanList, cpuList, outcomeList]
    
    while(True):
        
        hChoice = HumanPlayer(gameRecord)
        
        while (hChoice == 'G'):
            hChoice = HumanPlayer(gameRecord)
            
        if(hChoice == 'Q'):
            break
        
        cChoice = ComputerPlayer(gameRecord)
        outcome = Judge(cChoice, hChoice)
        PrintOutcome(outcome, cChoice, hChoice)
        UpdateGameRecord(gameRecord, cChoice, hChoice, outcome)
        
    print('Thank you for playing my game!')
    
# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
