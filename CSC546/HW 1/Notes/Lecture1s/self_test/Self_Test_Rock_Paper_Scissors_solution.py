# %% always put import statements at the very beginning
from random import randint

# %%
def HumanPlayer(RecordOfGame):    
    while True:        
        print("let's play ...................")
        print("rock(r), paper(p), scissors(s)?")
        print("or you want to see a record of the game (g)?")
        print("or you want to quit(q)?", end='')
        user_str= input("please make your choice now:")
        if user_str == 'rock' or user_str == 'paper' or user_str == 'scissors':
            ChoiceOfHumanPlayer = user_str
            break
        elif user_str == 'g':
            PrintRecordOfGame(RecordOfGame)
        elif user_str == 'quit':
            ChoiceOfHumanPlayer = 'quit'
            break
        else:
            print("The computer does not understand your input")
    return ChoiceOfHumanPlayer
# %%
def ComputerPlayer(RecordOfGame):
    ActionList = ("rock", "paper", "scissors")
    ChoiceOfComputerPlayer = ActionList[randint(0, 2)]    
    return ChoiceOfComputerPlayer
# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    Outcome = 0
    if ChoiceOfComputerPlayer == "paper" and ChoiceOfHumanPlayer == "scissors":
        Outcome = 2
    elif ChoiceOfComputerPlayer == "paper" and ChoiceOfHumanPlayer == "paper":
        Outcome = 0
    elif ChoiceOfComputerPlayer == "paper" and ChoiceOfHumanPlayer == "rock":
        Outcome = 1
    elif ChoiceOfComputerPlayer == "rock" and ChoiceOfHumanPlayer == "scissors":
        Outcome = 1
    elif ChoiceOfComputerPlayer == "rock" and ChoiceOfHumanPlayer == "paper":
        Outcome = 2
    elif ChoiceOfComputerPlayer == "rock" and ChoiceOfHumanPlayer == "rock":
        Outcome = 0
    elif ChoiceOfComputerPlayer == "scissors" and ChoiceOfHumanPlayer == "scissors":
        Outcome = 0
    elif ChoiceOfComputerPlayer == "scissors" and ChoiceOfHumanPlayer == "paper":
        Outcome = 1
    elif ChoiceOfComputerPlayer == "scissors" and ChoiceOfHumanPlayer == "rock":
        Outcome = 2
    else:
        print("Something is wrong @ Judge")
    return Outcome

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    print("-------------------------------Outcome---------------------------------------")
    if Outcome == 0:
        print("It is a tie: Computer chose", ChoiceOfComputerPlayer,
                              "Human chose", ChoiceOfHumanPlayer)
    elif Outcome == 1:
        print("Computer wins: Computer chose", ChoiceOfComputerPlayer, ";",
                                   "Human chose", ChoiceOfHumanPlayer)
    elif Outcome == 2:
        print("Human wins: Computer chose", ChoiceOfComputerPlayer, ";",
                                "Human chose", ChoiceOfHumanPlayer)
    print("-----------------------------------------------------------------------------")
# %%
def UpdateRecordOfGame(RecordOfGame, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    RecordOfGame["ComputerPlayer"].append(ChoiceOfComputerPlayer)
    RecordOfGame["HumanPlayer"].append(ChoiceOfHumanPlayer)
    RecordOfGame["Outcome"].append(Outcome)
# %%
def PrintRecordOfGame(RecordOfGame):
    c=0
    h=0
    for k in range(0, len(RecordOfGame["Outcome"])):
        Outcome = RecordOfGame["Outcome"][k]
        if Outcome == 1:
            c+=1
        elif Outcome == 2:
            h+=1           
    print("-------Record of the Game------")
    print("The number of rounds is", len(RecordOfGame["Outcome"]))
    print("Human wins", h, 'round(s)')
    print("Computer wins", c, 'round(s)')
    print("Human, Computer")
    for k in range(0, len(RecordOfGame["HumanPlayer"])):
        str1=RecordOfGame["HumanPlayer"][k]
        str2=RecordOfGame["ComputerPlayer"][k]
        print(str1, ',', str2)
    print("-------------------------------")

# %% the game
def PlayGame():
    print("Welcome to rock-paper-scissors !")
    RecordOfGame={"HumanPlayer":[], "ComputerPlayer":[], "Outcome":[]}
    while True:
        ChoiceOfComputerPlayer=ComputerPlayer(RecordOfGame)
        ChoiceOfHumanPlayer=HumanPlayer(RecordOfGame)
        if ChoiceOfHumanPlayer == 'quit':
            break
        Outcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        UpdateRecordOfGame(RecordOfGame, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome)
        PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)    
    print("------------GameOver----------")    

# %% play the game
if __name__ == '__main__':
    PlayGame()
