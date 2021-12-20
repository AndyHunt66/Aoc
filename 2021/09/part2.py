import copy
import sys
import re

# inFile = './testInput.txt'
inFile = './input.txt'

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

class colours:  # You may need to change color settings
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    ENDC = '\033[m'

class directions:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    MIDDLE = 5

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
def whereIsLower(j, i):
    # check up
    if j >= 1:
        if compare2spots(j - 1, i, j, i):
            return directions.UP

    # check down
    if j < caveYAxis - 1:
        if compare2spots(j + 1, i, j, i):
            return directions.DOWN

    # Check Left
    if i >= 1:
        if compare2spots(j, i - 1, j, i):
            return directions.LEFT

    # Check Right
    if i < caveXAxis - 1:
        if compare2spots(j, i + 1, j, i):
            return directions.RIGHT

    return directions.MIDDLE

def findBottom(a,b, searched):
    whereToGo = whereIsLower(a,b)
    # if whereToGo == directions.MIDDLE:
    #     # do nothing

    if whereToGo == directions.UP:
        nextPoint = Point(b,a-1)
    elif whereToGo == directions.DOWN:
        nextPoint = Point(b,a+1)
    elif whereToGo == directions.LEFT:
        nextPoint = Point(b-1,a)
    elif whereToGo == directions.RIGHT:
        nextPoint = Point(b+1,a)
    elif whereToGo == directions.MIDDLE:
        nextPoint = Point(-1,-1)


    searched.append(Point(b,a))
    if nextPoint.x != -1 and basins[nextPoint.y][nextPoint.x] == 0 :
        findBottom(nextPoint.y,nextPoint.x, searched)
    else:
        if nextPoint.x == -1:
            found = str(b)+","+str(a)
        else:
            found = basins[nextPoint.y][nextPoint.x]
        for coordinate in searched:
            basins[coordinate.y][coordinate.x] = found
            if found in basinsList:
                basinsList[found] += 1
            else:
                basinsList[found] = 1
        searched = []
    return(a,b)




caveFloor = []
basins = []
with open(inFile, 'r') as fh:
    for line in fh:
        caveFloor.append([int(x) for x in str(line.strip())])
        basins.append([0] * len(line))
caveXAxis = len(caveFloor[0])
caveYAxis = len(caveFloor)
basinsList = {}

for j in range(caveYAxis):
    for i in range(caveXAxis):
        if basins[j][i] != 0:
            continue
        if caveFloor[j][i] == 9:
            continue
        searched = []
        findBottom(j, i, searched)
printCaveFloor()
print("Cave floor width : ", caveXAxis)
print("Cave floor depth : ", caveYAxis)
#print("Basin Sizes: ", sorted(basinsList.values(), reverse=True))
print("Basin Sizes: ", basinsList.values())
biggest = sorted(basinsList.values(),reverse=True)[0:3]
print("Biggest basins: ",  biggest     )
print("Basins : ", basins)
print("Answer; ", biggest[0]*biggest[1]*biggest[2])
