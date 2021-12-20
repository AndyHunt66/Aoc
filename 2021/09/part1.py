import copy
import sys
import re

# inFile = './testInput.txt'
inFile = './input.txt'


class colours:  # You may need to change color settings
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    ENDC = '\033[m'


def printCaveFloor():
    print("CaveFloor : ")
    colour = colours.RED
    for xLine in caveFloor:
        printCommand = "";
        for floor in xLine:
            if floor == 9:
                colour = colours.RED
            if floor == 8 or floor == 7 or floor == 6:
                colour = colours.YELLOW
            if floor == 5 or floor == 4 or floor == 3:
                colour = colours.GREEN
            if floor == 2 or floor == 1 or floor == 0:
                colour = colours.BLUE
            printCommand += colour
            printCommand += str(floor)
        print(printCommand, colours.ENDC)


# True if the first coordinate pair is LOWER than the 2nd
def compare2spots(y, x, y1, x1):
    # print(y,x,y1,x1)
    return caveFloor[y][x] < caveFloor[y1][x1]


# j is vertical - row - YAxis
# i is horizonral - column - Xaxis
def isSpotLowest(j, i):
    # check up
    if j >= 1:
        if not compare2spots(j, i, j - 1, i):
            return False

    # check down
    if j < caveYAxis - 1:
        if not compare2spots(j, i, j + 1, i):
            return False

    # Check Left
    if i >= 1:
        if not compare2spots(j, i, j, i - 1):
            return False

    # Check Right
    if i < caveXAxis - 1:
        if not compare2spots(j, i, j, i + 1):
            return False

    return True


caveFloor = []
with open(inFile, 'r') as fh:
    for line in fh:
        caveFloor.append([int(x) for x in str(line.strip())])
caveXAxis = len(caveFloor[0])
caveYAxis = len(caveFloor)
risk = 0
for j in range(caveYAxis):
    for i in range(caveXAxis):
        if isSpotLowest(j, i):
            risk += caveFloor[j][i] + 1

printCaveFloor()
print("Cave floor width : ", caveXAxis)
print("Cave floor depth : ", caveYAxis)
print("Risk  ", risk)
