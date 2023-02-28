# Constants used
from statistics import mean

dirtyArea = {'A': 1, 'B': 1}
performance_ratings = []
CLEAN = 0
DIRTY = 1
ASIDE = 'A'
BSIDE = 'B'

# These are the same but for some reason the 'for each' loops further below doesnt work with only one
every_environment_A = [{ASIDE: CLEAN, BSIDE: CLEAN}, {ASIDE: CLEAN, BSIDE: DIRTY},
                       {ASIDE: DIRTY, BSIDE: CLEAN}, {ASIDE: DIRTY, BSIDE: DIRTY}]
every_environment_B = [{ASIDE: CLEAN, BSIDE: CLEAN}, {ASIDE: CLEAN, BSIDE: DIRTY},
                       {ASIDE: DIRTY, BSIDE: CLEAN}, {ASIDE: DIRTY, BSIDE: DIRTY}]


def reflexVaccum(view):
    # Given pseudocode:
    # if status = Dirty then return Suck
    # else if location = A then return Right
    # else if location = B then return Left

    location = view[0]
    status = view[1]
    if status == DIRTY:
        return -1
    elif location == ASIDE:
        return BSIDE
    elif location == BSIDE:
        return ASIDE


def VacuumAgent(agentProgram, startLocation):
    # Run for an arbitrary 10 steps, even though really this will always finish in at most 3 steps(suck, move, suck)

    currentLocation = startLocation
    performance = 0

    for i in range(10):
        nextStep = agentProgram((currentLocation, dirtyArea[currentLocation]))

        if nextStep == -1:
            performance += 10
            dirtyArea[currentLocation] = dirtyArea[currentLocation] - 1
            # Allows the user to change how 'dirty' areas are by changing the value in the maps if they wanted
            # and ensures the program still works without the strict constants of only 0 vs 1 (clean vs dirty)

        elif nextStep == ASIDE:
            performance -= 1
            currentLocation = ASIDE
        elif nextStep == BSIDE:
            performance -= 1
            currentLocation = BSIDE

    print("Area is totally clean: " + str(dirtyArea[ASIDE] == CLEAN and dirtyArea[BSIDE] == CLEAN))
    print("Agent's Performance: " + str(performance) + "\n")
    performance_ratings.append(performance)
    return performance


# Set up the area after the previous test and run the agent on that newly generated area
for starting_environment in every_environment_A:
    dirtyArea = starting_environment
    VacuumAgent(reflexVaccum, ASIDE)

for starting_environment in every_environment_B:
    dirtyArea = starting_environment
    VacuumAgent(reflexVaccum, BSIDE)

print(performance_ratings)
print(mean(performance_ratings))
