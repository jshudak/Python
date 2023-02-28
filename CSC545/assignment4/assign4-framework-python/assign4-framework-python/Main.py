import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population

statesToNumbers = {}


# Author Fan Zhang
def initMap(map):
    map.states.append("North Carolina")
    map.states.append("South Carolina")
    map.states.append("Virginia")
    map.states.append("Tennessee")
    map.states.append("Kentucky")
    map.states.append("West Virginia")
    map.states.append("Georgia")
    map.states.append("Alabama")
    map.states.append("Mississippi")
    map.states.append("Florida")

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
    populationSize = popSize # TODO find reasonable value
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

if __name__ == '__main__':
    runGeneticAlgorithm(10, 150, 0)
    runGeneticAlgorithm(500, 15000, 1)
