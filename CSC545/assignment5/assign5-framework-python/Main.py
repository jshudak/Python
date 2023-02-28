import random
import time
import copy

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population

statesToNumbers = {}
map = Map()


# Author Fan Zhang
def initMap(map):
    map.state_names.append("North Carolina")
    map.state_names.append("South Carolina")
    map.state_names.append("Virginia")
    map.state_names.append("Tennessee")
    map.state_names.append("Kentucky")
    map.state_names.append("West Virginia")
    map.state_names.append("Georgia")
    map.state_names.append("Alabama")
    map.state_names.append("Mississippi")
    map.state_names.append("Florida")

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))


def betterMap(map):
    statesFile = open("us_states_51_ij.txt", "r")
    stateEnumeration = 0
    for line in statesFile:
        startingState = ""
        border = line.split(",")
        for i, stateNL in enumerate(border):
            state = stateNL.strip()

            if state not in statesToNumbers.keys():
                map.states.append(state)
                statesToNumbers[state] = stateEnumeration
                stateEnumeration += 1

            if i == 0:
                startingState = state
                continue
            else:
                borderTuple = Border(statesToNumbers[startingState], statesToNumbers[state])
                map.borders.append(borderTuple)


def runGeneticAlgorithm(popSize, iterations, smallVsBig):
    map = Map()
    if smallVsBig == 0:
        initMap(map)
    else:
        betterMap(map)
    populationSize = popSize  # TODO find reasonable value
    population = Population(map, populationSize)

    maxIterations = iterations  # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map)  # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and goalFound == False:
        newPopulation = Population(map, 0)
        for i in range(populationSize):
            x = population.randomSelection()
            y = population.randomSelection()
            child = x.reproduce(y)
            if random.randint(0, 100) < 15:
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
                break
            newPopulation.vector.append(child)
            newPopulation.allFitness.append(child.fitness)
        currentIteration += 1
        population = newPopulation

    if goalFound:
        print("Found a solution after ", currentIteration, " iterations")
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ", currentIteration, " iterations")


def is_consistent(state, state_color, assignment, temp_csp):
    for border in temp_csp["Constraints"]:
        if len(assignment.genome) > border.index1 and len(assignment.genome) > border.index2:
            if border.index1 == state:
                if state_color == assignment.genome[border.index2]:
                    return False
            if border.index2 == state:
                if state_color == assignment.genome[border.index1]:
                    return False
    return True


def update_color_options(state, state_color, assignment, temp_csp):
    for border in temp_csp["Constraints"]:
        if border.index1 == state and border.index2 >= len(assignment.genome):
            if temp_csp["States"][border.index2].count(state_color) == 1:
                temp_csp["States"][border.index2].remove(state_color)
        if border.index2 == state and border.index1 >= len(assignment.genome):
            if temp_csp["States"][border.index1].count(state_color) == 1:
                temp_csp["States"][border.index1].remove(state_color)
        if len(temp_csp["States"][border.index1]) == 0 or len(temp_csp["States"][border.index2]) == 0:
            return None
    return temp_csp


def check_arcs(state, assignment, temp_csp):
    reserve_csp = copy.deepcopy(temp_csp)
    neighbors = []
    for border in temp_csp["Constraints"]:
        if border.index1 == state:
            neighbors.append(border.index2)
        if border.index2 == state:
            neighbors.append(border.index1)

    remove_colors = []

    for color in temp_csp["States"][state]:
        temp_csp = copy.deepcopy(reserve_csp)
        pred_csp = update_color_options(state, color, assignment, temp_csp)
        if pred_csp is None:
            remove_colors.append(color)
            continue

        for neighbor in neighbors:
            if len(pred_csp["States"][neighbor]) == 0:
                remove_colors.append(color)
                continue

    for color in remove_colors:
        temp_csp["States"][state].remove(color)
    return temp_csp


def recursive_backtracking(temp_csp, assignment=Individual(map)):
    if assignment.isGoal():
        print("Goal found!")
        return assignment

    nextState = assignment.chosen
    if nextState == len(map.state_names):
        return False

    for color in temp_csp["States"][nextState]:
        if is_consistent(nextState, color, assignment, temp_csp):
            new_assignment = Individual(map, assignment.genome + color)
            result = recursive_backtracking(temp_csp.copy(), new_assignment)
            if result != False:
                return result

    return False


def backtracking_WFC(temp_csp, assignment=Individual(map)):
    if assignment.isGoal():
        return assignment

    nextState = assignment.chosen
    if nextState == len(map.state_names):
        return False

    for color in temp_csp["States"][nextState]:
        if is_consistent(nextState, color, assignment, temp_csp):
            updatedValues = update_color_options(nextState, color, assignment, temp_csp.copy())
            if updatedValues is None:
                continue
            new_assignment = Individual(map, assignment.genome + color)
            result = backtracking_WFC(updatedValues, new_assignment)
            if result != False:
                return result

    return False


def backtracking_AC3(temp_csp, assignment=Individual(map)):
    if assignment.isGoal():
        print("Goal found!")
        return assignment

    nextState = assignment.chosen
    if nextState == len(map.state_names):
        return False

    temp_csp = check_arcs(nextState, assignment, temp_csp.copy())
    if temp_csp is None:
        return False

    for color in temp_csp["States"][nextState]:
        if is_consistent(nextState, color, assignment, temp_csp):
            new_assignment = Individual(map, assignment.genome + color)
            result = backtracking_AC3(temp_csp.copy(), new_assignment)
            if result != False:
                return result

    return False


def min_conflicts(temp_csp, max_conflicts, current=Individual(map)):
    current.generateGenome()

    for max in range(max_conflicts):
        if current.isGoal():
            return current

        state = pick_random_conflict(current, temp_csp)
        best_color = find_min_conflict(state, current, csp)[1]
        new_genome = ""
        for i in range(state):
            new_genome += current.genome[i]
        new_genome += str(best_color)
        for i in range(state+1, len(current.genome)):
            new_genome += current.genome[i]

        current.genome = new_genome
        current.updateFitness()

    return current


def pick_random_conflict(assignment, csp):
    state = random.randint(0, 9)
    while is_consistent(state, assignment.genome[state], assignment, csp):
        state = random.randint(0, 9)
    return state


def find_min_conflict(state, assignment, csp):
    min_conflicts = (len(csp["Constraints"]), 9)

    for color in range(4):
        current_conflicts = 0
        for border in csp["Constraints"]:
            if border.index1 == state:
                if color == assignment.genome[border.index2]:
                    current_conflicts += 1
            if border.index2 == state:
                if color == assignment.genome[border.index1]:
                    current_conflicts += 1
        if min_conflicts[0] > current_conflicts:
            min_conflicts = (current_conflicts, color)

    return min_conflicts


def refresh_csp():
    states_and_colors = {}
    for i in range(10):
        states_and_colors[i] = ["0", "1", "2", "3"]
    constraints = map.borders
    temp_csp = {"States": states_and_colors, "Constraints": constraints}
    return temp_csp


if __name__ == '__main__':
    initMap(map)

    csp = refresh_csp()
    print("-------- Backtracking with initial --------")
    start = time.time()
    backtracking_with_initial = recursive_backtracking(csp, Individual(map, "1"))
    end = time.time()
    print("Backtracking with initialization finished after " + str(end - start) + " seconds.")
    backtracking_with_initial.printresult()

    csp = refresh_csp()
    print("\n\n-------- Backtracking without initial --------")
    start = time.time()
    backtracking_without_initial = recursive_backtracking(csp, Individual(map))
    end = time.time()
    print("Backtracking without initialization finished after " + str(end - start) + "seconds.")
    backtracking_without_initial.printresult()

    csp = refresh_csp()
    print("\n\n-------- Backtrack with Forward Checking with initial --------")
    start = time.time()
    backtracking_with_FWC_initial = backtracking_WFC(csp, Individual(map, "2"))
    end = time.time()
    print("Finished after " + str(end - start) + " seconds.")
    backtracking_with_FWC_initial.printresult()

    csp = refresh_csp()
    print("\n\n-------- Backtracking with Forward Checking without initial --------")
    start = time.time()
    backtracking_with_FWC = backtracking_WFC(csp, Individual(map))
    end = time.time()
    print("Finished after " + str(end - start) + "seconds.")
    backtracking_with_FWC.printresult()

    csp = refresh_csp()
    print("\n\n-------- Backtrack with AC-3 with initial --------")
    start = time.time()
    backtracking_with_AC3_initial = backtracking_AC3(csp, Individual(map, "1"))
    end = time.time()
    print("Finished after " + str(end - start) + " seconds.")
    backtracking_with_AC3_initial.printresult()

    csp = refresh_csp()
    print("\n\n-------- Backtracking with AC-3 without initial --------")
    start = time.time()
    backtracking_with_AC3 = backtracking_AC3(csp, Individual(map))
    end = time.time()
    print("Finished after " + str(end - start) + " seconds.")
    backtracking_with_AC3.printresult()

    csp = refresh_csp()
    print("\n\n-------- min_conflicts with initial --------")
    start = time.time()
    min_conflict_initial = min_conflicts(csp, 500, Individual(map, "1"))
    end = time.time()
    print("Finished after " + str(end - start) + " seconds.")
    min_conflict_initial.printresult()

    csp = refresh_csp()
    print("\n\n-------- min_conflicts without initial --------")
    start = time.time()
    min_conflict_noinit = min_conflicts(csp, 500, Individual(map))
    end = time.time()
    print("Finished after " + str(end - start) + " seconds.")
    min_conflict_noinit.printresult()
