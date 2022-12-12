import sys


# inFile = './testInput.txt'
inFile = './input.txt'


def checkNextMoves():
    endpoint = flatCavern.index("E")
    # for startingpoint in range(0,len(flatCavern)-1):
    startingpoint = flatCavern.index("S")
    routeCosts[startingpoint] = 0
    while startingpoint < len(flatCavern):
        print(startingpoint)

        if flatCavern[startingpoint] == "E" or routeCosts[startingpoint] == sys.maxsize:
            startingpoint += 1
            continue
        if flatCavern[startingpoint] == "S":
            currentHeight = "a"
        else:
            currentHeight = flatCavern[startingpoint]

        ## Ugh... horrible
        flatCavern[endpoint] = "z"

        rightMove = startingpoint + 1
        downMove = startingpoint + cavernWidth
        leftMove = startingpoint - 1
        upMove = startingpoint - cavernWidth

        if (rightMove % cavernWidth) != 0 and (rightMove <= len(flatCavern)-1):
            if ord(flatCavern[rightMove]) <= ord(currentHeight)+1:
                routeCosts[rightMove] = min(routeCosts[startingpoint] + 1, routeCosts[rightMove])

        if downMove <= len(flatCavern)-1:
            if ord(flatCavern[downMove]) <= ord(currentHeight)+1:
                routeCosts[downMove] = min(routeCosts[startingpoint] + 1, routeCosts[downMove])

        if (startingpoint % cavernWidth) != 0 and leftMove > 0:
            if ord(flatCavern[leftMove]) <= ord(currentHeight)+1:
                if (routeCosts[startingpoint] + 1) < routeCosts[leftMove]:
                    # print("Uhoh - Left Move from need to do some more work here" , startingpoint)
                    # print("   previous cost: ", routeCosts[leftMove])
                    # print("   new cost     : ", routeCosts[startingpoint] + flatCavern[leftMove])
                    routeCosts[leftMove] = routeCosts[startingpoint] + 1
                    startingpoint = leftMove
                    continue

        if upMove > 0:
            if ord(flatCavern[upMove]) <= ord(currentHeight)+1:
                if (routeCosts[startingpoint] + 1) < routeCosts[upMove]:
                    # print("Uhoh - Up Move from need to do some more work here" , startingpoint)
                    routeCosts[upMove] = routeCosts[startingpoint] + 1
                    startingpoint = upMove
                    continue

        ## Ugh... horrible
        flatCavern[endpoint] = "E"

        startingpoint += 1


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
        cavern.append(list(line.strip()))
        cavernWidth = len(line.strip())
        routeCosts = routeCosts + [sys.maxsize] * cavernWidth
flatCavern = list(textCavern)
routeCosts[0] = 0

# print ("CavernWidth: ", cavernWidth)
# for row in cavern:
#     print(row)
# print(flatCavern)
# exit()
currentPoint = 0

checkNextMoves()
print("Position of End: {0}".format([flatCavern.index("E")]))
print("Width:", cavernWidth)
print("Part 1 Answer is ", routeCosts[flatCavern.index("E")])
