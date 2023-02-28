import random


# Author Fan Zhang
class Individual:

    # Updates the fitness value based on the genome and the map.
    def updateFitness(self):
        self.fitness = 0
        for border in self.map.borders:
            if len(self.genome) > border.index1 and len(self.genome) > border.index2:
                if self.genome[border.index1] != self.genome[border.index2]:
                    self.fitness += 1

    def __init__(self, map, gene=""):
        self.map = map  # the map
        self.maxLen = len(self.map.state_names)
        self.fitness = 0  # fitness is cached and only updated on request whenever necessary
        self.chosen = len(gene)
        self.genome = gene
        self.updateFitness()

    def generateGenome(self):
        while len(self.genome) != self.maxLen:
            numberGen = int(random.randint(0, 99) / 25)
            self.genome += str(numberGen)

    # Reproduces a child randomly from two individuals (see textbook).
    # x The first parent.
    # y The second parent.
    # return The child created from the two individuals.
    def reproduce(self, y):
        child = Individual(self.map)
        randomSplit = random.randint(1, self.maxLen - 1)
        child.genome = self.genome[:randomSplit] + y.genome[randomSplit:]
        child.updateFitness()
        return child

    # Randomly mutates the individual.
    # Randomize more than 1 gene to try and help 50 state algorithm find an answer.
    # Unnecessary for the smaller map but still works!
    def mutate(self):
        for i in range(random.randint(0, 5)):
            randomMutation = random.randint(0, 3)
            randomGene = random.randint(0, self.maxLen - 1)
            genomeAsList = list(self.genome)
            genomeAsList[randomGene] = str(randomMutation)
            self.genome = "".join(genomeAsList)
        self.updateFitness()

    # Checks whether the individual represents a valid goal state.
    # return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        print("Your result:")
        print("Final genome: " + self.genome)
        print("fitness: " + str(self.fitness))
        for i, state in enumerate(self.map.state_names):
            print(state + ": " + self.genome[i])
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
