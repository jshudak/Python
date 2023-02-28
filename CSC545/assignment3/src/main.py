#! /usr/bin/env python3
import math
import shapely.geometry
from shapely.geometry import LineString

from environment import Environment
from vector2d import Vector2D


class Node:
    def __init__(self, parent, vector, h, g):
        self.parent = parent
        self.vector = vector
        self.gcost = g
        self.hcost = h
        self.fcost = h + g
        self.computef()

    def computef(self):
        self.fcost = self.gcost + self.hcost

    def __str__(self):
        return "Node at (" + str(self.vector.x) + ", " + str(self.vector.y) + ") with a f = " + str(
            self.fcost) + ", h= " + str(self.hcost) + ", g = " + str(self.gcost)


def greedySearch(env):
    #
    # TODO: return a path from start to goal using greedy search
    #
    return []


def uniformCostSearch(env):
    #
    # TODO
    #
    return []


def findLowestCost(givenNodes):
    lowestCost = 9999
    bestNode = None
    for node in givenNodes:
        if node.fcost < lowestCost:
            bestNode = node
            lowestCost = node.fcost

    return bestNode


def climbChild(Node):
    toReturn = []
    while Node.parent is not None:
        toReturn.append(Node.vector)
        print(Node.parent)
        Node = Node.parent
    toReturn.append(Node.vector)
    return toReturn


def unpackTree(tree):
    toReturn = []
    for elem in tree:
        toReturn.append(elem.vector)
    return toReturn


def astarSearch(env):

    startState = Node(None, env.start, env.start.dist(env.goal), 0)
    goalState = env.goal
    currentTree = [startState]
    allPolygons = []
    allVerticies = []
    for poly in env.obstacles:
        toBePoly = []
        for vector in poly.vertices:
            allVerticies.append(vector)
            toBePoly.append((vector.x, vector.y))
        allPolygons.append(shapely.geometry.Polygon(toBePoly))
    allVerticies.append(goalState)
    visited = []

    while True:
        bestNode = findLowestCost(currentTree)
        visited.append(bestNode.vector)

        if bestNode.vector == goalState:
            return climbChild(bestNode)

        currentTree.remove(bestNode)

        print("Searching Node: " + str(bestNode))

        bestNodeTuple = (bestNode.vector.x, bestNode.vector.y)

        for vert in allVerticies:
            makeNode = True
            if vert not in visited:
                vertAsTuple = (vert.x, vert.y)
                testLine = LineString([bestNodeTuple, vertAsTuple])
                for poly in allPolygons:
                    if testLine.crosses(poly) or poly.contains(testLine):
                        makeNode = False
                        break
                if makeNode:
                    parent = bestNode
                    gcost = vert.dist(bestNode.vector) + bestNode.gcost
                    hcost = goalState.dist(vert)
                    newNode = Node(parent, vert, hcost, gcost)
                    currentTree.append(newNode)
                    print("Made a node!")

    return unpackTree(currentTree)


if __name__ == '__main__':
    env = Environment('output/environment.txt')
    print("Loaded an environment with {} obstacles.".format(len(env.obstacles)))

    searches = {
        'greedy': greedySearch,
        'uniformcost': uniformCostSearch,
        'astar': astarSearch
    }

    for name, fun in searches.items():
        print("Attempting a search with " + name)
        Environment.printPath(name, fun(env))
