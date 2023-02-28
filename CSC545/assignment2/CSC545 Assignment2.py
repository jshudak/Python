goalState = ((0, 0), (0, 0), (3, 3))
visitedStates = set()
answerKey = []

def BreadthFirstSearch(startNode):
    # Start with a queue that has the starting state
    searchQueue = []
    searchQueue.append(startNode)

    while searchQueue:
        # Get the next state and say it has been visited. If its the answer, success!
        # Also, assume this is part of the answer unless proven otherwise.
        currentState = searchQueue.pop()
        visitedStates.add(currentState)
        answerKey.append(currentState)
        if currentState == goalState:
            return "Answer found!"

        newMoves = makeNewMoves(currentState, searchQueue)

        # If the current state led us nowhere, it is not part of the answer.
        if not newMoves:
            answerKey.remove(currentState)

        for move in newMoves:
            searchQueue.append(move)

    # If the queue ends up empty, it did not find an answer.
    return "absolutely failed."


def makeNewMoves(currentState, frontier):
    allMoves = []
    newMoves = []
    leftSide = currentState[0]
    boat = currentState[1]
    rightSide = currentState[2]

    # Not the most efficient way, but describes all moves that can be made:
    # The left side can interact with the boat by moving 1, 2, or (1, 1) object from left to boat and vice versa
    # This same idea also occurs between the right side and the boat
    for i in range(1, 3):
        allMoves.append(((leftSide[0] - i, leftSide[1]), (boat[0] + i, boat[1]), rightSide))
        allMoves.append(((leftSide[0], leftSide[1] - i), (boat[0], boat[1] + i), rightSide))
        allMoves.append(((leftSide[0] + i, leftSide[1]), (boat[0] - i, boat[1]), rightSide))
        allMoves.append(((leftSide[0], leftSide[1] + i), (boat[0], boat[1] - i), rightSide))
        allMoves.append((leftSide, (boat[0] - i, boat[1]), (rightSide[0] + i, rightSide[1])))
        allMoves.append((leftSide, (boat[0], boat[1] - i), (rightSide[0], rightSide[1] + i)))
        allMoves.append((leftSide, (boat[0] + i, boat[1]), (rightSide[0] - i, rightSide[1])))
        allMoves.append((leftSide, (boat[0], boat[1] + i), (rightSide[0], rightSide[1] - i)))
    allMoves.append(((leftSide[0] - 1, leftSide[1] - 1), (boat[0] + 1, boat[1] + 1), rightSide))
    allMoves.append(((leftSide[0] + 1, leftSide[1] + 1), (boat[0] - 1, boat[1] - 1), rightSide))
    allMoves.append((leftSide, (boat[0] + 1, boat[1] + 1), (rightSide[0] - 1, rightSide[1] - 1)))
    allMoves.append((leftSide, (boat[0] - 1, boat[1] - 1), (rightSide[0] + 1, rightSide[1] + 1)))

    # Now that we've gathered all moves, we only want the valid ones.
    # Im sure theres an efficient way to check and generate at the same time, but this works!
    for move in allMoves:
        if isValidMove(move, frontier):
            newMoves.append(move)

    return newMoves

def isValidMove(node, frontier):
    if node in visitedStates or node in frontier:
        return False

    if node == goalState:
        return True

    for i in range(3):
        for j in range(2):
            if node[i][j] < 0:
                return False

    if node[0][0] >= node[0][1] and node[2][0] >= node[2][1] and (0 < node[1][0] + node[1][1] <= 2) and node[0][
        0] < 4 and node[0][1] < 4 and node[2][0] < 4 and node[2][1] < 4:
        return True

    return False


def main():
    startNode = ((3, 3), (0, 0), (0, 0))

    print(BreadthFirstSearch(startNode))
    for state in answerKey:
        print(str(state))


main()

# Notes used to help visualize the different actions that can be taken
# Each node describes the number of sheep and wolves ((on the left), (on the boat), (on the right))
# To solve the riddle the following steps must be taken:
# 1: ((3, 3), (0, 0), (0, 0))
# 2: ((2, 2), (1, 1), (0, 0))
# 3: ((2, 2), (1, 0), (0, 1))
# 4: ((2, 1), (1, 1), (0, 1))
# 5: ((2, 1), (0, 1), (1, 1))
# 6: ((1, 1), (1, 1), (1, 1))
# 7: ((1, 1), (0, 1), (2, 1))
# 8: ((0, 1), (1, 1), (2, 1))
# 9: ((0, 1), (0, 1), (3, 1))
# 10:((0, 0), (0, 2), (3, 1))
# 11:((0, 0), (0, 0), (3, 3))
