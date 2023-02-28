# Class representing a population of individuals
# Author Fan Zhang
import math
import random

from Individual import Individual


class Population:
    # Actual standard ctor.
    # param map The map.
    # param initialSize The initial size of the population.
    def __init__(self, map, initialSize):
        self.allFitness = []
        self.vector = []
        for i in range(initialSize):
            self.vector.append(Individual(map))
            self.allFitness.append(self.vector[-1].fitness)

    # Randomly selects an individual out of the population
    # proportionally to its fitness.
    # return The selected individual.
    def randomSelection(self):
        # an individual should be selected with a probability
        # proportional to its fitness
        return (random.choices(population=self.vector, weights=self.allFitness, k=1))[0]

    def bestFitness(self):
        return str(max(self.allFitness))
