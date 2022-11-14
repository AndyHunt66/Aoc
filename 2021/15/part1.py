from itertools import combinations_with_replacement, product
from  more_itertools import nth_combination, distinct_combinations

import copy

#inFile = './tinyTest.txt'
#inFile = './testInput1.txt'
inFile = './input.txt'

def checkNextMoves(startingPoint: int):
    rightMove = startingPoint + 1
    downMove = startingPoint + cavernWidth
    if (rightMove % cavernWidth ) != 0 and (rightMove <= len(flatCavern)-1):
        if routeCosts[rightMove] != 0:
#            routeCosts[rightMove] = min(routeCosts[startingPoint] + flatCavern[rightMove], routeCosts[rightMove])
            if routeCosts[startingPoint] + flatCavern[rightMove] < routeCosts[rightMove]:
                ## New lowest cost path to this point
                routes[rightMove] = routes[startingPoint] + 'R'
                routeCosts[rightMove] = routeCosts[startingPoint] + flatCavern[rightMove]

        else:
            routeCosts[rightMove] = routeCosts[startingPoint] + flatCavern[rightMove]
            routes[rightMove] = routes[startingPoint] + 'R'


    if (downMove <= len(flatCavern)-1):
        if routeCosts[downMove] != 0:
            # routeCosts[downMove] = min(routeCosts[startingPoint] + flatCavern[downMove], routeCosts[downMove])
            if routeCosts[startingPoint] + flatCavern[downMove] < routeCosts[downMove]:
                routeCosts[downMove] = routeCosts[startingPoint] + flatCavern[downMove]
                routes[downMove] = routes[startingPoint] + 'D'
        else:
            routeCosts[downMove] = routeCosts[startingPoint] + flatCavern[downMove]
            routes[downMove] = routes[startingPoint] + 'D'


cavern = []
flatCavern = []
routeCosts = []
routes = []
textCavern = ''
cavernWidth = 0
with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        cavern.append(list(map(int, line.strip())))
        textCavern += line.strip()
        cavernWidth = len(line.strip())
        routeCosts = routeCosts + [0] * cavernWidth
        routes = routes + ['>'] * cavernWidth
flatCavern = list(map(int, textCavern))

for row in cavern:
    print(row)
print ("CavernWidth: ", cavernWidth)
print(flatCavern)
print(routeCosts)
# What's the cheapest 2 move from here?
currentPoint = 0
for i in range(0, len(flatCavern)-1):
    print("Checking number ", i)
    checkNextMoves(i)

print ("Done")
print(flatCavern)
print(routeCosts)

