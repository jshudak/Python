# class that implements the MiniMax algorithm.
import random
import sys

import Square
from TicTacToeAction import TicTacToeAction


class MiniMax:
    def __init__(self):
        self.numberOfStates = 0  # < counter to measure the number of iterations / states.
        self.usePruning = False

    # Start procedure of the MiniMax algorithm.
    # state: The state where the MiniMax algorithm starts searching
    # usePruning: Whether to use alpha - beta - pruning
    # return An optimal action to be taken at this point.
    def MinimaxDecision(self, state, usePruning):
        self.usePruning = usePruning
        self.numberOfStates = 0
        print(state)
        # TODO Implement the minimax decision routine.Iterate over all possible actions
        #  and evaluate their utilitiesinvoking MinValue().Return the action that
        #  generates the highest utility.
        #  You can just return the first or the last best action, however it makes
        #  the algorithm way more interesting if you determine all best actions
        #  and thenselect one of them randomly.
        v = -999999
        best = TicTacToeAction('Broken', -1)
        for a in state.getActions():
            print("Putting " + a.player + " at " + str(a.position))
            if v < self.MinValue(state, -999999, 99999):
                best = a

        print("Placing at: " + str(best.position))
        print("State space size: ", self.numberOfStates)
        return best

    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # return The minimum of the utilites invoking MaxValue, or the utility of the state if it is a leaf.
    def MinValue(self, state, alpha, beta):
        self.numberOfStates += 1
        # TODO implement the MinValue procedure according to the textbook:
        #  function Min - Value(state, alpha, beta) return a utility value
        #       if TERMINAL - TEST(state) then return UTILITY(state)
        #       v < - +infinity
        #       for each a in ACTIONS(State) do
        #           v < - min(v, MAX-VALUE(RESULT(state, a), alpha, beta))
        #           if MiniMax.usePruning then
        #               if v <= alpha then return v
        #               beta < - min(beta, v)
        #       return v
        # The pseudo code is slightly changed to be able to reuse the code for alpha-beta-pruning.
        if state.isTerminal():
            return state.getUtility()
        v = 99999999
        for a in state.getActions():
            v = min(v, self.MaxValue(state.getResult(a), alpha, beta))
            if self.usePruning:
                if v <= alpha:
                    return v
                beta = min(beta, v)
        return v

    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # The maximum of the utilites invoking MinValue, or the utility of the state if it is a leaf.
    def MaxValue(self, state, alpha, beta):
        self.numberOfStates += 1
        # TODO implement the MaxValue procedure according to the textbook:
        #  function Max - Value(state, alpha, beta) return a utility value
        #       if TERMINAL - TEST(state) then return UTILITY(state)
        #       v < - -infinity
        #       for each a in ACTIONS(State) do
        #           v < - max(v, MIN-VALUE(RESULT(state, a), alpha, beta))
        #           if MiniMax.usePruning then
        #               if v >= beta then return v
        #               alpha < - max(alpha, v)
        #       return v
        # The pseudo code is slightly changed to be able to reuse the * code for alpha-beta-pruning.
        if state.isTerminal():
            return state.getUtility()
        v = -99999999
        for a in state.getActions():
            v = max(v, self.MinValue(state.getResult(a), alpha, beta))
            if self.usePruning:
                if v >= beta:
                    return v
                alpha = max(alpha, v)
        return v
