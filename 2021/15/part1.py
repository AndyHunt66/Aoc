# inFile = './tinyTest.txt'
# inFile = './testInput1.txt'
inFile = './input.txt'


def checkNextMoves(startingpoint: int):
    rightMove = startingpoint + 1
    downMove = startingpoint + cavernWidth
    if (rightMove % cavernWidth) != 0 and (rightMove <= len(flatCavern)-1):
        if routeCosts[rightMove] != 0:
            routeCosts[rightMove] = min(routeCosts[startingpoint] + flatCavern[rightMove], routeCosts[rightMove])
        else:
            routeCosts[rightMove] = routeCosts[startingpoint] + flatCavern[rightMove]

    if downMove <= len(flatCavern)-1:
        if routeCosts[downMove] != 0:
            routeCosts[downMove] = min(routeCosts[startingpoint] + flatCavern[downMove], routeCosts[downMove])
        else:
            routeCosts[downMove] = routeCosts[startingpoint] + flatCavern[downMove]


flatCavern = []
routeCosts = []
cavernWidth = 0
textCavern = ''
with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        textCavern += line.strip()
        cavernWidth = len(line.strip())
        routeCosts = routeCosts + [0] * cavernWidth
flatCavern = list(map(int, textCavern))

# print ("CavernWidth: ", cavernWidth)
# print(flatCavern)
currentPoint = 0
for i in range(0, len(flatCavern)-1):
    # print("Checking number ", i)
    checkNextMoves(i)

# print(flatCavern)
# print(routeCosts)
print("Answer is ", routeCosts[-1])
