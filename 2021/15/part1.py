import copy
import sys
import time

# inFile = './tinyTest.txt'
# inFile = './testInput1.txt'
inFile = './input.txt'


def checkNextMoves():

    # for startingpoint in range(0,len(flatCavern)-1):
    startingpoint = 0
    while startingpoint < len(flatCavern):
        rightMove = startingpoint + 1
        downMove = startingpoint + cavernWidth
        leftMove = startingpoint - 1
        upMove = startingpoint - cavernWidth

        if (rightMove % cavernWidth) != 0 and (rightMove <= len(flatCavern)-1):
            routeCosts[rightMove] = min(routeCosts[startingpoint] + flatCavern[rightMove], routeCosts[rightMove])

        if downMove <= len(flatCavern)-1:
            routeCosts[downMove] = min(routeCosts[startingpoint] + flatCavern[downMove], routeCosts[downMove])

        if (startingpoint % cavernWidth) != 0 and leftMove > 0:
            if (routeCosts[startingpoint] + flatCavern[leftMove]) < routeCosts[leftMove]:
                # print("Uhoh - Left Move from need to do some more work here" , startingpoint)
                # print("   previous cost: ", routeCosts[leftMove])
                # print("   new cost     : ", routeCosts[startingpoint] + flatCavern[leftMove])
                routeCosts[leftMove] = routeCosts[startingpoint] + flatCavern[leftMove]
                startingpoint = leftMove
                continue

        if upMove > 0:
            if (routeCosts[startingpoint] + flatCavern[upMove]) < routeCosts[upMove]:
                # print("Uhoh - Up Move from need to do some more work here" , startingpoint)
                routeCosts[upMove] = routeCosts[startingpoint] + flatCavern[upMove]
                startingpoint = upMove
                continue
        startingpoint += 1


def increaseMap(multiple: int) -> []:
    largerCavern = copy.deepcopy(cavern)
    # Each horizontal row slice goes up +1
    # Then each vertical entire row goes up +1
    for j in range(1, multiple):
        for increaserow in largerCavern:
            # Horizontal expansion
            increaserow.extend([x + j if (x + j) < 10 else (x + j - 9) for x in increaserow[0:cavernWidth]])

    for j in range(1, multiple):
        # Vertical Expansion
        for k in range(len(cavern)):
            largerCavern.append([x + j if (x + j) < 10 else (x + j - 9) for x in largerCavern[k][0:cavernWidth*multiple]])

    return largerCavern


start = time.process_time()

cavern = []
flatCavern = []
routeCosts = []
cavernWidth = 0
textCavern = ''

with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        textCavern += line.strip()
        cavern.append(list(map(int, line.strip())))
        cavernWidth = len(line.strip())
        routeCosts = routeCosts + [sys.maxsize] * cavernWidth
flatCavern = list(map(int, textCavern))
routeCosts[0] = 0
# print ("CavernWidth: ", cavernWidth)
# for row in cavern:
#     print(row)
# print(flatCavern)
currentPoint = 0

checkNextMoves()

print("Part 1 Answer is ", routeCosts[-1])
print(time.process_time() - start)

# Part 2
bigCavern = increaseMap(5)
cavernWidth = len(bigCavern[0])
flatCavern = [i for j in bigCavern for i in j]
routeCosts = [sys.maxsize for i in range(len(flatCavern))]
routeCosts[0] = 0
#
checkNextMoves()
print("Part 2 Answer is ", routeCosts[-1])

# your code here
print(time.process_time() - start)
