#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction

finishedStates = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 5, 8],
    [2, 5, 6]
]

class TicTacToeState:


    # Updates the utility value.
    def updateUtility(self):
        print ("Updates the utility value.")
        # TODO The utility value for the TicTacToe game is defined as follows:
        #   - if player has three marks in a row, it is 1
        #   - if the other player has three marks in a row, it is -1
        #   - otherwise it is 0
        #   Note tha "three marks in a row" can actually be a row, a column
        #   or a diagonal.So basically, first find out if there are three
        #   identical values in a row, and if so, check whether the marks belong
        #   to player or not.
        for state in finishedStates:
            if self.field[state[0]] == self.field[state[1]] == self.field[state[2]]:
                if self.field[state[0]] == self.player:
                    return 1
                else:
                    return -1
        return 0


    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player, either X or O.
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).

    def getActions(self):
        #  TODO For the TicTacToe game, there is one valid action
        #   for each empty square.The action would then consist
        #   of the position of the empty square and the "color" of
        #   the player to move.
        print("getActions")
        actions = []
        for i, space in enumerate(self.field):
            if space != 'X' and space != 'O':
                actions.append(TicTacToeAction(self.player, i))
        return actions

    def getUtility(self):
        return self.utility

    def getResult(self,action):
        #TODO Create a new state and copy all the contents of the current state
        #  to the new one (in particular the field and the player).
        # The player to move must be switched. Then incorporate the action into
        # the field of the new state. Finally, compute the utility of the new state using updateUtility().
        print("getResult")
        state = TicTacToeState()
        state.field = self.field
        state.player = self.player
        state.field[action.position] = action.player
        if action.player == 'X':
            state.playerToMove = 'O'
        else:
            state.playerToMove = 'X'
        state.updateUtility()
        return state

    def  isTerminal(self):
        #TODO Hint: the utility value has specific values if one of
        # the players has won, which is a terminal state. However,
        # you will also have to check for terminal states in which
        # no player has won, which can not be inferred immediately
        # from the utility value.
        if self.field.count('X') + self.field.count('O') == 9 or self.utility != 0:
            return True
        return False

    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)